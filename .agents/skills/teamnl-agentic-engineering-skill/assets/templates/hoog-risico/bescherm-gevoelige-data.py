#!/usr/bin/env python3
"""Beschermhook bij risiconiveau hoog, voor Claude Code, Codex, GitHub Copilot en Mistral Vibe.

Onderdeel van de teamnl-agentic-engineering-skill. Hoort in het project op
.agents/hooks/bescherm-gevoelige-data.py. Elke agent roept het aan vanuit zijn
eigen hookconfiguratie, met --agent claude, codex, copilot of vibe.

Vooraf, bij elke toolaanroep:
- weigert het acties die gevoelige paden raken, ook via shellcommando's,
  zoekopdrachten, patches, jokertekens en recursief zoeken vanuit een
  bovenliggende map;
- weigert het shellcommando's met de echte-data-sleutel TEAMNL_ECHTE_DATA, en
  alle shellcommando's als die sleutel in de omgeving van de agent staat.

Achteraf maskeert het herkenbare persoonsnummers in de uitvoer, voordat het
model die ziet, voor zover de agent dat ondersteunt.

De verboden paden komen uit de Read- en Edit-deny-regels in .claude/settings.json
en .claude/settings.local.json van het project. Dat is de enige lijst, ook voor
de andere agents.

Het script faalt dicht: bij een interne fout weigert het de actie, in het
formaat van de agent. Meldingen noemen nooit het pad of de waarde zelf, alleen
de regel.

Dit is een extra slot, geen kluis. Daarom staat bij risiconiveau hoog de echte
data buiten de repo en gebruikt de code de echte-data-sleutel.

Zelftest: python bescherm-gevoelige-data.py --zelftest
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

WINDOWS = os.name == "nt"
AGENTS = ("claude", "codex", "copilot", "vibe")
SLEUTEL = "TEAMNL_ECHTE_DATA"

# Herkenbare persoonsnummers. Houd deze lijst gelijk aan .gitleaks.toml en aan
# references/veilig-verwerken.md van de skill.
PATRONEN = [
    re.compile(r"\b[A-NP-Z]{2}[A-NP-Z0-9]{6}[0-9]\b"),  # paspoort- of ID-kaartnummer (NL)
    re.compile(r"\b[0-9]{9}\b"),  # negen cijfers: mogelijk een BSN
    re.compile(r"\b[PI][A-Z<][A-Z]{3}[A-Z0-9<]{25,}"),  # eerste MRZ-regel van een reisdocument
    re.compile(r"[A-Z0-9<]{9}[0-9][A-Z<]{3}[0-9]{6}[0-9][MFX<][0-9]{6}[0-9]"),  # tweede MRZ-regel
]
MASKER = "[GEMASKEERD]"

# Soorten tools, op naam (in kleine letters, de laatste naamdelen na een punt).
SHELL_NAMEN = {"bash", "powershell", "shell", "exec_command", "process_start", "process_write",
               "local_shell", "run_in_terminal", "write_bash", "write_powershell"}
LEES_NAMEN = {"read", "read_file", "view", "view_image", "grep", "rg", "glob", "ls", "list_dir", "search"}
PAD_VELDEN = ("file_path", "filePath", "path", "notebook_path", "file", "filename", "cwd", "dir",
              "directory", "paths", "files", "target", "source", "destination")
SHELL_VELDEN = ("command", "cmd", "script")
INVOER_VELDEN = ("input", "text")  # tekst die naar een draaiende shell gaat
UITVOER_VELDEN = ("toolResult", "tool_result", "tool_response", "tool_output_text")
PATCH_KOP = re.compile(r"^\*\*\* (?:Add File|Update File|Delete File|Move to): (.+?)\s*$", re.M)

# Commando's die mappen recursief doorzoeken. Een heuristiek: liever te vaak
# weigeren dan een map met gevoelige data doorzoeken.
RECURSIEF = re.compile(
    r"\b(?:grep|egrep|fgrep|zgrep|cp|scp|chmod|chown|zip)\b[^|;&]*?\s-[a-zA-Z]*[rR]"
    r"|\bls\b[^|;&]*?\s-[a-zA-Z]*R"
    r"|(?i:\b(?:gci|dir|ls|get-childitem|select-string)\b[^|;&]*?\s-r(?:ecurse)?\b)"
    r"|--recursive\b|(?:^|\s)/[sS](?=\s|$)"
    r"|(?:^|[;&|(`]\s*)(?:find|tree|du|rsync|tar|7z|robocopy|xcopy)\b"
    r"|\bos\.walk\b|\brglob\b|recursive\s*=\s*True"
    r"|\brg\b[^|;&]*?(?:\s-u+\b|--no-ignore)"
)
SCHEIDING = re.compile(r"[\s'\"`;|&<>(){}\[\],=]+")
TUSSEN_AANHALINGSTEKENS = re.compile(r"\"([^\"]*)\"|'([^']*)'")
JOKERTEKENS = re.compile(r"[*?]")

MELDING = (
    "Geweigerd door de TeamNL-beschermhook (risiconiveau hoog): deze actie valt onder {}. "
    "Werk met fictieve data in data/example/ of tests/fixtures/. Zoek je tekst in de code? "
    "Doorzoek dan een concrete map, zoals src/. Is dit onterecht? Leg het voor aan de "
    "gebruiker en verruim de blokkade niet zelf."
)
MELDING_MASKER = (
    "[TeamNL-beschermhook: de uitvoer bevatte herkenbare persoonsnummers en is gemaskeerd. "
    "Pas de code aan zodat die geen waarden toont, alleen aantallen of rij- en kolomnummers.]"
)


# ---------------------------------------------------------------- paden

def normaliseer(pad):
    """Zet een pad in de vorm /c/map/bestand, zoals Claude Code dat ook doet."""
    pad = pad.strip().replace("\\", "/")
    m = re.match(r"^([A-Za-z]):(?:/|$)", pad)
    if m:
        pad = "/" + m.group(1).lower() + pad[2:]
    return pad


def os_pad(pad):
    """Zet een genormaliseerd pad terug in de vorm die het besturingssysteem kent."""
    if WINDOWS:
        m = re.match(r"^/([a-zA-Z])(?:/|$)", pad)
        if m:
            return m.group(1).upper() + ":/" + pad[3:]
    return pad


def absoluut(pad, basis):
    """Maakt een pad absoluut ten opzichte van basis en lost . en .. op."""
    pad = normaliseer(pad)
    if pad == "~" or pad.startswith("~/"):
        pad = normaliseer(os.path.expanduser("~")) + pad[1:]
    if not pad.startswith("/"):
        pad = basis.rstrip("/") + "/" + pad
    delen = []
    for deel in pad.split("/"):
        if deel in ("", "."):
            continue
        if deel == "..":
            if delen:
                delen.pop()
            continue
        delen.append(deel)
    return "/" + "/".join(delen)


def glob_naar_regex(glob):
    """Zet een glob in gitignore-stijl om naar een reguliere expressie."""
    i, uit = 0, []
    while i < len(glob):
        if glob.startswith("**/", i):
            uit.append("(?:.*/)?")
            i += 3
        elif glob.startswith("**", i):
            uit.append(".*")
            i += 2
        elif glob[i] == "*":
            uit.append("[^/]*")
            i += 1
        elif glob[i] == "?":
            uit.append("[^/]")
            i += 1
        else:
            uit.append(re.escape(glob[i]))
            i += 1
    return re.compile("".join(uit), re.IGNORECASE if WINDOWS else 0)


def gelijk_of_onder(pad, map_):
    """Is pad gelijk aan map_ of ligt het eronder?"""
    if WINDOWS:
        pad, map_ = pad.lower(), map_.lower()
    map_ = map_.rstrip("/")
    return map_ == "" or pad == map_ or pad.startswith(map_ + "/")


class Regel:
    """Een deny-regel, met een voorbeeldpad voor de controles op jokertekens en mappen."""

    def __init__(self, soort, patroon, project, cwd):
        self.soort = soort  # "Read" of "Edit"
        self.origineel = soort + "(" + patroon + ")"
        if patroon.startswith("//"):
            glob = "/" + patroon[2:]  # absoluut pad
        elif patroon.startswith("~/"):
            glob = normaliseer(os.path.expanduser("~")) + patroon[1:]
        elif patroon.startswith("/"):
            glob = project + patroon  # ten opzichte van de projectroot
        elif patroon.startswith("**/") or "/" not in patroon.rstrip("/"):
            glob = patroon if patroon.startswith("**/") else "**/" + patroon  # overal
        else:
            glob = cwd + "/" + (patroon[2:] if patroon.startswith("./") else patroon)
        self.regex = glob_naar_regex(glob)
        voorbeeld = project + "/" + glob[3:] if glob.startswith("**/") else glob
        is_map = voorbeeld.endswith("/**")
        voorbeeld = re.sub(r"/\*\*$", "/x", voorbeeld)
        self.voorbeeld = voorbeeld.replace("**", "x").replace("*", "x").replace("?", "x")
        self.plek = self.voorbeeld[:-2] if is_map else self.voorbeeld

    def raakt(self, pad):
        return bool(self.regex.fullmatch(pad) or self.regex.fullmatch(pad + "/x"))

    def raakt_joker(self, pad):
        """Kan een pad met jokertekens deze regel raken?"""
        if glob_naar_regex(pad).fullmatch(self.voorbeeld):
            return True
        delen, vb = pad.split("/"), self.voorbeeld.split("/")
        for k, stuk in enumerate(delen):
            if JOKERTEKENS.search(stuk):
                if "**" not in stuk and k < len(vb):  # ** beslaat meerdere mappen
                    prefix = "/".join(vb[: k + 1])
                    if glob_naar_regex("/".join(delen[: k + 1])).fullmatch(prefix):
                        return gelijk_of_onder(prefix, self.plek)
                return False
        return False


def lees_regels(project, cwd):
    """Leest de Read- en Edit-deny-regels uit de projectinstellingen."""
    regels, uitzonderingen = [], []
    for naam in ("settings.json", "settings.local.json"):
        bestand = os.path.join(os_pad(project), ".claude", naam)
        if not os.path.exists(bestand):
            continue
        with open(bestand, encoding="utf-8") as f:
            deny = json.load(f).get("permissions", {}).get("deny", [])
        for item in deny:
            m = re.fullmatch(r"(Read|Edit)\((.+)\)", item.strip())
            if not m:
                continue
            soort, patroon = m.groups()
            if patroon.startswith("!"):
                uitzonderingen.append(Regel(soort, patroon[1:], project, cwd))
            else:
                regels.append(Regel(soort, patroon, project, cwd))
    if not any(r.soort == "Read" for r in regels):
        raise RuntimeError("geen Read-deny-regels gevonden in .claude/settings.json")
    return regels, uitzonderingen


# ---------------------------------------------------------------- beoordelen

def controleer_pad(pad, regels, uitzonderingen, soorten):
    """Geeft de geraakte regel terug, of None."""
    joker = bool(JOKERTEKENS.search(pad))
    for r in regels:
        if r.soort not in soorten:
            continue
        if joker:
            if r.raakt_joker(pad):
                return r.origineel
        elif r.raakt(pad) and not any(
            u.soort == r.soort and u.regex.fullmatch(pad) for u in uitzonderingen
        ):
            return r.origineel
    return None


def splits_commando(commando):
    """Haalt mogelijke paden uit een commando; tekst tussen aanhalingstekens blijft ook heel."""
    tokens = []
    for m in TUSSEN_AANHALINGSTEKENS.finditer(commando):
        inhoud = m.group(1) if m.group(1) is not None else m.group(2)
        tokens.append(inhoud)
        tokens.extend(SCHEIDING.split(inhoud))
    tokens.extend(SCHEIDING.split(TUSSEN_AANHALINGSTEKENS.sub(" ", commando)))
    return [t for t in tokens if t.strip() and not t.startswith("-")]


def beoordeel_shell(commando, cwd, regels, uitzonderingen):
    paden = [absoluut(t, cwd) for t in splits_commando(commando)]
    for pad in paden:
        geraakt = controleer_pad(pad, regels, uitzonderingen, {"Read", "Edit"})
        if geraakt:
            return geraakt
    if not RECURSIEF.search(commando):
        return None
    mappen = []
    for pad in paden:
        delen = pad.split("/")
        for i, stuk in enumerate(delen):
            if JOKERTEKENS.search(stuk):
                pad = "/".join(delen[:i]) or "/"
                break
        if pad == "/" or os.path.exists(os_pad(pad)):
            mappen.append(pad)
    if not mappen:
        mappen.append(cwd)  # geen bestaand doel genoemd: de huidige map
    for map_ in mappen:
        for r in regels:
            if r.soort == "Read" and gelijk_of_onder(r.plek, map_):
                return r.origineel
    return None


def als_tekst(waarde):
    """Zet een commando (tekst of lijst met argumenten) om naar een tekst."""
    if isinstance(waarde, list):
        return " ".join('"' + str(w) + '"' if " " in str(w) else str(w) for w in waarde)
    return str(waarde)


def lees_actie(invoer):
    """Haalt fase, korte toolnaam en toolinvoer uit de invoer, ongeacht de agent."""
    gebeurtenis = str(invoer.get("hook_event_name") or invoer.get("hookEventName") or "")
    if gebeurtenis:
        fase = "na" if gebeurtenis.lower().replace("_", "").startswith("post") else "voor"
    else:  # Copilot noemt de gebeurtenis niet; achteraf staat het resultaat erbij
        fase = "na" if any(v in invoer for v in UITVOER_VELDEN) else "voor"
    tool = str(invoer.get("tool_name") or invoer.get("toolName") or "")
    ti = invoer.get("tool_input", invoer.get("toolArgs", invoer.get("toolInput", {})))
    if isinstance(ti, str):
        try:
            ti = json.loads(ti)
        except ValueError:
            ti = {"command": ti}
    if not isinstance(ti, dict):
        ti = {}
    kort = tool.lower().split(".")[-1]
    return fase, tool, kort, ti


def is_shell_naam(kort, tool):
    """Herkent ook namen met een punt, zoals process.start (Vibe)."""
    return kort in SHELL_NAMEN or tool.lower().replace(".", "_") in SHELL_NAMEN


def soort_tool(kort, ti, tool=""):
    if is_shell_naam(kort, tool):
        return "shell"
    if kort == "apply_patch" or any(isinstance(v, str) and "*** Begin Patch" in v for v in ti.values()):
        return "patch"
    if kort in LEES_NAMEN:
        return "lezen"
    if any(ti.get(v) for v in SHELL_VELDEN):
        return "shell"
    return "schrijven"  # onbekend: streng beoordelen, op lees- en schrijfregels


def paden_uit(kort, soort, ti):
    paden = []
    for veld in PAD_VELDEN:
        waarde = ti.get(veld)
        if isinstance(waarde, str) and waarde:
            paden.append(waarde)
        elif isinstance(waarde, list):
            paden.extend(str(w) for w in waarde if w)
    if kort == "glob" and ti.get("pattern"):
        paden.append(str(ti.get("path") or ".").rstrip("/\\") + "/" + str(ti["pattern"]))
    if soort == "patch":
        for waarde in ti.values():
            if isinstance(waarde, str):
                paden.extend(PATCH_KOP.findall(waarde))
    return paden


def beoordeel(invoer, project):
    """Geeft de geraakte regel terug als de actie geweigerd moet worden, anders None."""
    project = normaliseer(os.path.abspath(project))
    cwd = normaliseer(os.path.abspath(invoer.get("cwd") or project))
    regels, uitzonderingen = lees_regels(project, cwd)
    _, tool, kort, ti = lees_actie(invoer)
    soort = soort_tool(kort, ti, tool)
    if soort == "shell":
        velden = SHELL_VELDEN + (INVOER_VELDEN if is_shell_naam(kort, tool) else ())
        commando = " ".join(als_tekst(ti[v]) for v in velden if ti.get(v))
        omgeving = ti.get("env") if isinstance(ti.get("env"), dict) else {}
        if SLEUTEL in commando or SLEUTEL in omgeving:
            return "de echte-data-sleutel " + SLEUTEL
        if os.environ.get(SLEUTEL):
            return "de echte-data-sleutel " + SLEUTEL + ", die in de omgeving van de agent staat"
        geraakt = beoordeel_shell(commando, cwd, regels, uitzonderingen)
        if geraakt:
            return geraakt
    soorten = {"Read"} if soort == "lezen" else {"Read", "Edit"}
    for pad in paden_uit(kort, soort, ti):
        geraakt = controleer_pad(absoluut(pad, cwd), regels, uitzonderingen, soorten)
        if geraakt:
            return geraakt
    return None


# ---------------------------------------------------------------- maskeren

def maskeer_tekst(tekst):
    for patroon in PATRONEN:
        tekst = patroon.sub(MASKER, tekst)
    return tekst


def maskeer_uitvoer(antwoord):
    """Geeft de gemaskeerde uitvoer terug, of None als er niets te maskeren was."""
    if isinstance(antwoord, str):
        nieuw = maskeer_tekst(antwoord)
        return nieuw if nieuw != antwoord else None
    if isinstance(antwoord, dict):
        nieuw = {k: maskeer_tekst(v) if isinstance(v, str) else v for k, v in antwoord.items()}
        return nieuw if nieuw != antwoord else None
    return None


def uitvoer_als_tekst(antwoord):
    if isinstance(antwoord, dict):
        return "\n".join(str(v) for k, v in antwoord.items() if isinstance(v, str) and v)
    return "" if antwoord is None else str(antwoord)


# ---------------------------------------------------------------- antwoorden per agent
# Elke functie geeft (exitcode, stdout, stderr) terug.

def weiger(agent, reden):
    tekst = MELDING.format(reden)
    if agent == "codex":
        return 0, json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse", "permissionDecision": "deny",
            "permissionDecisionReason": tekst}}), ""
    if agent == "vibe":
        return 0, json.dumps({"decision": "deny", "reason": tekst}), ""
    if agent == "copilot":
        return 0, json.dumps({"permissionDecision": "deny", "permissionDecisionReason": tekst}), ""
    return 2, "", tekst  # claude: exit 2, reden op stderr


def vervang_uitvoer(agent, tool, invoer, verborgen=False):
    """Maskeert de uitvoer achteraf. Geeft None als er niets te doen is."""
    if agent == "claude":
        if tool not in ("Bash", "PowerShell"):
            return None
        antwoord = invoer.get("tool_response")
        nieuw = ({"stdout": "[uitvoer verborgen: fout in de TeamNL-beschermhook]", "stderr": ""}
                 if verborgen else maskeer_uitvoer(antwoord))
        if nieuw is None:
            return None
        if verborgen and isinstance(antwoord, dict):
            nieuw = dict(antwoord, **nieuw)
        return 0, json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse", "updatedToolOutput": nieuw,
            "additionalContext": MELDING_MASKER}}), ""
    if agent == "vibe":
        tekst = str(invoer.get("tool_output_text") or "")
    elif agent == "codex":
        tekst = uitvoer_als_tekst(invoer.get("tool_response"))
    else:  # copilot
        resultaat = invoer.get("toolResult", invoer.get("tool_result"))
        if isinstance(resultaat, dict):
            resultaat = resultaat.get("textResultForLlm", resultaat.get("text_result_for_llm", ""))
        tekst = uitvoer_als_tekst(resultaat)
    if verborgen:
        nieuw = "[uitvoer verborgen: fout in de TeamNL-beschermhook]"
    else:
        nieuw = maskeer_tekst(tekst)
        if nieuw == tekst:
            return None
        nieuw += "\n" + MELDING_MASKER
    if agent == "vibe":
        return 0, json.dumps({"decision": "deny", "reason": nieuw}), ""
    if agent == "codex":
        return 0, json.dumps({"decision": "block", "reason": nieuw}), ""
    return 0, json.dumps({"modifiedResult": {"resultType": "success", "textResultForLlm": nieuw}}), ""


# ---------------------------------------------------------------- hoofdprogramma

def herken_agent(invoer):
    gebeurtenis = str(invoer.get("hook_event_name") or "")
    if gebeurtenis in ("pre_tool", "post_tool"):
        return "vibe"
    if "toolName" in invoer or "toolArgs" in invoer:
        return "copilot"
    if "turn_id" in invoer:
        return "codex"
    return "claude"


def projectmap(invoer):
    """De projectroot: twee mappen boven dit script (.agents/hooks/), anders uit de omgeving."""
    hier = Path(__file__).resolve().parents[2]
    if (hier / ".claude" / "settings.json").exists():
        return str(hier)
    return os.environ.get("CLAUDE_PROJECT_DIR") or invoer.get("cwd") or os.getcwd()


def hoofd(tekst, agent=None, project=None):
    """Verwerkt de invoer van een hook. Geeft (exitcode, stdout, stderr) terug."""
    invoer = json.loads(tekst)
    agent = agent or herken_agent(invoer)
    project = project or projectmap(invoer)
    fase, tool, _, _ = lees_actie(invoer)
    if fase == "na":
        try:
            resultaat = vervang_uitvoer(agent, tool, invoer)
        except Exception:
            resultaat = vervang_uitvoer(agent, tool, invoer, verborgen=True)
        return resultaat or (0, "", "")
    regel = beoordeel(invoer, project)
    return weiger(agent, regel) if regel else (0, "", "")


def argument(naam):
    if naam in sys.argv:
        i = sys.argv.index(naam)
        return sys.argv[i + 1] if i + 1 < len(sys.argv) else None
    return None


def main():
    if "--zelftest" in sys.argv:
        return zelftest()
    agent = argument("--agent")
    if agent not in AGENTS:
        agent = None
    tekst = ""
    try:
        tekst = sys.stdin.read()
        code, uit, fout = hoofd(tekst, agent)
    except Exception as e:  # faal dicht, in het formaat van de agent
        if agent is None:
            try:
                agent = herken_agent(json.loads(tekst))
            except Exception:
                agent = "claude"
        code, uit, fout = weiger(agent, "een fout in de hook zelf (" + type(e).__name__
                                 + "); laat de gebruiker de hook controleren met --zelftest")
    if uit:
        sys.stdout.write(uit)
    if fout:
        sys.stderr.write(fout + "\n")
    return code


# ---------------------------------------------------------------- zelftest

def zelftest():
    """Test de beoordeling in een tijdelijk nepproject, voor alle agents. Toont geen inhoud."""
    fouten, totaal = 0, 0

    def controleer(omschrijving, goed):
        nonlocal fouten, totaal
        totaal += 1
        if not goed:
            fouten += 1
            print("MISLUKT: " + omschrijving)

    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "project met spatie")
        extern = os.path.join(tmp, "externe-data")
        bestanden = [".env", ".env.example", "data/private/a.csv", "data/example/b.csv",
                     "output/r.csv", "logs/runtime/app.log", "src/x.py", "requirements.txt"]
        for pad in [os.path.join(p, b) for b in bestanden] + [os.path.join(extern, "p.csv")]:
            os.makedirs(os.path.dirname(pad), exist_ok=True)
            with open(pad, "w", encoding="utf-8") as f:
                f.write("nep\n")
        instellingen = {"permissions": {"deny": [
            "Read(**/.env)", "Read(**/.env.*)", "Read(!**/.env.example)",
            "Read(**/data/private/**)", "Read(**/media/private/**)",
            "Read(/output/**)", "Read(/logs/runtime/**)", "Read(/tmp/**)",
            "Read(/" + normaliseer(extern) + "/**)",
            "Edit(/.claude/settings.json)", "Edit(/.claude/settings.local.json)", "Edit(/.agents/hooks/**)",
            "Edit(/.codex/**)", "Edit(/.github/hooks/**)", "Edit(/.github/copilot/**)", "Edit(/.vibe/**)",
        ]}}
        os.makedirs(os.path.join(p, ".claude"))
        with open(os.path.join(p, ".claude", "settings.json"), "w", encoding="utf-8") as f:
            json.dump(instellingen, f)

        def claude(tool, ti):
            return {"hook_event_name": "PreToolUse", "cwd": p, "tool_name": tool, "tool_input": ti}

        p_win, p_posix = p.replace("/", "\\"), normaliseer(p)
        # 1. Beoordeling, met de toolnamen van Claude Code: (omschrijving, invoer, geweigerd verwacht)
        gevallen = [
            ("Read .env", claude("Read", {"file_path": p + "/.env"}), True),
            ("Read .env.example", claude("Read", {"file_path": p + "/.env.example"}), False),
            ("Read privédata met Windows-pad", claude("Read", {"file_path": p_win + "\\data\\private\\a.csv"}), True),
            ("Read broncode", claude("Read", {"file_path": p + "/src/x.py"}), False),
            ("Read externe datamap", claude("Read", {"file_path": os.path.join(extern, "p.csv")}), True),
            ("Read runtime-log", claude("Read", {"file_path": p + "/logs/runtime/app.log"}), True),
            ("cat .env", claude("Bash", {"command": "cat .env"}), True),
            ("cat .env.example", claude("Bash", {"command": "cat .env.example"}), False),
            ("grep -rn in de root", claude("Bash", {"command": "grep -rn S01 ."}), True),
            ("grep -rn zonder pad", claude("Bash", {"command": "grep -rn S01"}), True),
            ("grep in een bestand", claude("Bash", {"command": "grep -n S01 src/x.py"}), False),
            ("grep -rn in src", claude("Bash", {"command": "grep -rn S01 src"}), False),
            ("ls data", claude("Bash", {"command": "ls data"}), False),
            ("ls -lrt", claude("Bash", {"command": "ls -lrt"}), False),
            ("ls -R data", claude("Bash", {"command": "ls -R data"}), True),
            ("pip install -r", claude("Bash", {"command": "pip install -r requirements.txt"}), False),
            ("python opent privédata", claude("Bash", {"command": "python -c \"open('data/private/a.csv').read()\""}), True),
            ("python met os.walk", claude("Bash", {"command": "python -c \"import os; print(list(os.walk('.')))\""}), True),
            ("jokerteken in een map", claude("Bash", {"command": "cat data/priv*/a.csv"}), True),
            ("jokertekens in twee mappen", claude("Bash", {"command": "cat data/*/*"}), True),
            ("jokerteken voor .env", claude("Bash", {"command": "cat .e*"}), True),
            ("runtime-log met tail", claude("Bash", {"command": "tail logs/runtime/app.log"}), True),
            ("find in de root", claude("Bash", {"command": "find . -name '*.csv'"}), True),
            ("absoluut Windows-pad met spatie", claude("Bash", {"command": "type \"" + p_win + "\\output\\r.csv\""}), True),
            ("absoluut POSIX-pad met spatie", claude("Bash", {"command": "cat '" + p_posix + "/.env'"}), True),
            ("tests draaien", claude("Bash", {"command": "pytest -q"}), False),
            ("git status", claude("Bash", {"command": "git status"}), False),
            ("instellingen wijzigen via de shell", claude("Bash", {"command": "sed -i s/a/b/ .claude/settings.json"}), True),
            ("hookconfig van Codex wijzigen", claude("Bash", {"command": "echo x > .codex/hooks.json"}), True),
            ("sleutel in commando", claude("Bash", {"command": SLEUTEL + "=1 python -m app"}), True),
            ("sleutel in PowerShell", claude("PowerShell", {"command": "$env:" + SLEUTEL + " = '1'; python -m app"}), True),
            ("PowerShell .env", claude("PowerShell", {"command": "Get-Content .\\.env"}), True),
            ("PowerShell recursief", claude("PowerShell", {"command": "Get-ChildItem -Recurse data"}), True),
            ("PowerShell src", claude("PowerShell", {"command": "Get-ChildItem src -ErrorAction SilentlyContinue"}), False),
            ("Grep in privédata", claude("Grep", {"pattern": "S01", "path": "data/private"}), True),
            ("Grep in src", claude("Grep", {"pattern": "S01", "path": "src"}), False),
            ("Grep zonder pad", claude("Grep", {"pattern": "S01"}), False),
            ("Glob op privédata", claude("Glob", {"pattern": "data/private/*"}), True),
            ("Glob op Python-bestanden", claude("Glob", {"pattern": "**/*.py"}), False),
            ("Edit instellingen", claude("Edit", {"file_path": p + "/.claude/settings.json"}), True),
            ("Write in output", claude("Write", {"file_path": p + "/output/x.csv"}), True),
            ("Write in src", claude("Write", {"file_path": p + "/src/nieuw.py"}), False),
            # Codex: Bash met een commando, apply_patch met patchtekst, view_image met een pad
            ("Codex: cat .env", {"hook_event_name": "PreToolUse", "turn_id": "t", "cwd": p,
                                 "tool_name": "Bash", "tool_input": {"command": "cat .env"}}, True),
            ("Codex: patch op privédata", {"hook_event_name": "PreToolUse", "turn_id": "t", "cwd": p,
                                           "tool_name": "apply_patch", "tool_input": {"command":
                                           "*** Begin Patch\n*** Add File: data/private/n.csv\n+x\n*** End Patch\n"}}, True),
            ("Codex: patch op src", {"hook_event_name": "PreToolUse", "turn_id": "t", "cwd": p,
                                     "tool_name": "apply_patch", "tool_input": {"command":
                                     "*** Begin Patch\n*** Update File: src/x.py\n@@\n-a\n+b\n*** End Patch\n"}}, False),
            ("Codex: view_image in privémedia", {"hook_event_name": "PreToolUse", "turn_id": "t", "cwd": p,
                                                 "tool_name": "view_image", "tool_input": {"path": "media/private/foto.jpg"}}, True),
            # Vibe: volledige toolnamen met punt, process_start met env
            ("Vibe: read_file .env", {"hook_event_name": "pre_tool", "cwd": p, "tool_name": "file_system.read_file",
                                      "tool_input": {"file_path": ".env"}}, True),
            ("Vibe: bash grep -r", {"hook_event_name": "pre_tool", "cwd": p, "tool_name": "file_system.bash",
                                    "tool_input": {"command": "grep -r S01 ."}}, True),
            ("Vibe: edit in src", {"hook_event_name": "pre_tool", "cwd": p, "tool_name": "file_system.edit",
                                   "tool_input": {"file_path": "src/x.py", "old_string": "a", "new_string": "b"}}, False),
            ("Vibe: process.start met sleutel in env", {"hook_event_name": "pre_tool", "cwd": p,
                                                        "tool_name": "process.start", "tool_input":
                                                        {"command": "python -m app", "env": {SLEUTEL: "1"}}}, True),
            ("Vibe: process.write naar een shell", {"hook_event_name": "pre_tool", "cwd": p,
                                                    "tool_name": "process.write", "tool_input":
                                                    {"processId": "1", "text": "cat .env"}}, True),
            # Copilot: toolArgs als JSON-tekst of als object
            ("Copilot: bash cat .env", {"toolName": "bash", "cwd": p,
                                        "toolArgs": json.dumps({"command": "cat .env"})}, True),
            ("Copilot: view privédata", {"toolName": "view", "cwd": p, "toolArgs": {"path": "data/private/a.csv"}}, True),
            ("Copilot: view src", {"toolName": "view", "cwd": p, "toolArgs": json.dumps({"path": "src/x.py"})}, False),
            ("Copilot: hooks uitzetten", {"toolName": "create", "cwd": p,
                                          "toolArgs": {"path": ".github/copilot/settings.json"}}, True),
            ("Copilot: write_bash naar een shell", {"toolName": "write_bash", "cwd": p,
                                                    "toolArgs": {"input": "grep -r S01 ."}}, True),
            ("Onbekende tool met pad naar privédata", claude("mcp__fs__read", {"path": "data/private/a.csv"}), True),
        ]
        for omschrijving, invoer, verwacht in gevallen:
            controleer(omschrijving + " (verwacht: " + ("geweigerd" if verwacht else "toegestaan") + ")",
                       (beoordeel(invoer, p) is not None) == verwacht)

        # 2. Sleutel in de omgeving van de agent: elk shellcommando geweigerd.
        os.environ[SLEUTEL] = "1"
        try:
            controleer("sleutel in de omgeving", beoordeel(claude("Bash", {"command": "ls"}), p) is not None)
        finally:
            del os.environ[SLEUTEL]

        # 3. Weigerformaat per agent.
        verwacht_formaat = {
            "claude": lambda c, o, f: c == 2 and "Read(**/.env)" in f,
            "codex": lambda c, o, f: c == 0 and json.loads(o)["hookSpecificOutput"]["permissionDecision"] == "deny",
            "vibe": lambda c, o, f: c == 0 and json.loads(o)["decision"] == "deny",
            "copilot": lambda c, o, f: c == 0 and json.loads(o)["permissionDecision"] == "deny",
        }
        for agent, klopt in verwacht_formaat.items():
            c, o, f = hoofd(json.dumps(claude("Read", {"file_path": p + "/.env"})), agent, p)
            controleer("weigerformaat " + agent, klopt(c, o, f))

        # 4. Maskeren. De nepwaarden staan in delen, zodat Gitleaks dit bestand niet meldt.
        nep = "XX" + "1234567"
        c, o, f = hoofd(json.dumps({"hook_event_name": "PostToolUse", "tool_name": "Bash", "cwd": p,
                                    "tool_response": {"stdout": "rij 3: " + nep, "stderr": "", "interrupted": False}}),
                        "claude", p)
        nieuw = json.loads(o)["hookSpecificOutput"]["updatedToolOutput"] if o else {}
        controleer("maskeren claude", nep not in o and "interrupted" in nieuw and MASKER in nieuw.get("stdout", ""))
        c, o, f = hoofd(json.dumps({"hook_event_name": "post_tool", "tool_name": "file_system.read_file", "cwd": p,
                                    "tool_output_text": "rij 3: " + nep}), "vibe", p)
        controleer("maskeren vibe", nep not in o and json.loads(o)["decision"] == "deny")
        c, o, f = hoofd(json.dumps({"hook_event_name": "PostToolUse", "turn_id": "t", "tool_name": "Bash", "cwd": p,
                                    "tool_response": "rij 3: " + nep}), "codex", p)
        controleer("maskeren codex", nep not in o and json.loads(o)["decision"] == "block")
        c, o, f = hoofd(json.dumps({"toolName": "bash", "cwd": p, "toolArgs": {"command": "python -m app"},
                                    "toolResult": {"resultType": "success", "textResultForLlm": "rij 3: " + nep}}),
                        "copilot", p)
        controleer("maskeren copilot", nep not in o and MASKER in json.loads(o)["modifiedResult"]["textResultForLlm"])
        c, o, f = hoofd(json.dumps({"hook_event_name": "PostToolUse", "tool_name": "Bash", "cwd": p,
                                    "tool_response": {"stdout": "3 rijen verwerkt", "stderr": ""}}), "claude", p)
        controleer("uitvoer zonder persoonsnummers blijft ongewijzigd", o == "")

        # 5. Faalt dicht: kapotte invoer en ontbrekende instellingen.
        try:
            hoofd("geen json", "claude", p)
            controleer("kapotte invoer geweigerd", False)
        except ValueError:
            controleer("kapotte invoer geweigerd", True)
        os.remove(os.path.join(p, ".claude", "settings.json"))
        try:
            beoordeel(claude("Read", {"file_path": p + "/src/x.py"}), p)
            controleer("zonder instellingen geweigerd", False)
        except RuntimeError:
            controleer("zonder instellingen geweigerd", True)

    print("Zelftest: " + str(totaal - fouten) + " van " + str(totaal) + " geslaagd.")
    return 1 if fouten else 0


if __name__ == "__main__":
    sys.exit(main())
