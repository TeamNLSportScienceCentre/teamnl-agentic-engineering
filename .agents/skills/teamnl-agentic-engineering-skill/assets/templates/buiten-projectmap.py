"""Projectmap-hook voor Claude Code (TeamNL-basis).

Vraagt om toestemming als de agent buiten de projectmap leest of zoekt. Zo kijkt
een agent niet ongemerkt in je gebruikersmap, OneDrive of andere projecten.

Het script staat in .agents/hooks/buiten-projectmap.py. Claude Code roept het
aan vanuit .claude/settings.json (PreToolUse, voor Read, Grep, Glob, Bash en
PowerShell).

Zonder vragen toegestaan:
- de projectmap (CLAUDE_PROJECT_DIR) en alles daaronder;
- ~/.claude: instellingen, geheugen en skills van de agent;
- de tijdelijke map (TEMP, TMP, TMPDIR), waar de agent kladbestanden zet;
- permissions.additionalDirectories uit de instellingen van de gebruiker en
  van het project;
- de mappen in .claude/toegestane-mappen.txt van dit project. Zet daar één pad
  per regel in, met # voor commentaar. Het bestand staat buiten Git, omdat paden
  per computer verschillen. Zet er alleen een map in na akkoord van de gebruiker
  en leg de keuze vast in docs/decisions.md.

Al het andere geeft een toestemmingsvraag. Zet BESLISSING op "deny" om het hard
te blokkeren.

Read, Grep en Glob controleert het script precies. Bij Bash en PowerShell zoekt
het met een heuristiek naar paden in het commando. Een pad dat een script of een
variabele zelf opbouwt, ziet het niet. Dit is een vangnet tegen vergissingen,
geen beveiligingsgrens.

Bij een fout in dit script gaat de actie door: de hook mag het werk niet blokkeren.

Zelftest: python .agents/hooks/buiten-projectmap.py --zelftest
Vereist Python 3.8 of nieuwer en alleen de standaardbibliotheek.
"""
import json
import os
import re
import sys
import tempfile

BESLISSING = "ask"  # "ask" = eerst vragen, "deny" = altijd blokkeren
UITZONDERINGEN = os.path.join(".claude", "toegestane-mappen.txt")  # relatief aan de projectmap

QUOTED = re.compile(r'"([^"]*)"|\'([^\']*)\'')
# Begin van een absoluut pad: Windows (C:\ of C:/), Git Bash (/c/), POSIX (/Users/...) of de thuismap.
ABS_START = re.compile(
    r'^(?:[A-Za-z]:[\\/]|/[A-Za-z]|~(?:[\\/]|$)|\$HOME\b|\$\{HOME\}|\$env:USERPROFILE\b|%USERPROFILE%)',
    re.I)
# Absolute paden los in een commando. Niet na een letter, punt of slash, zodat
# URL's, Git-refs (origin/main) en sed-expressies (s/a/b/) niet meetellen.
EMBEDDED = re.compile(r'(?<![\w/.:~$-])(?:[A-Za-z]:[\\/]|/[A-Za-z][\w.-]*/)[^\s"\'`|;&<>()]*')
HOMEISH = re.compile(
    r'(?<![\w$])(?:~(?=[\\/\s;|&)]|$)|\$HOME\b|\$\{HOME\}|\$env:USERPROFILE\b|%USERPROFILE%)'
    r'[^\s"\'`|;&<>()]*', re.I)
PARENT = re.compile(r'(?<![\w.])\.\.(?![.\w])(?:[\\/][^\s"\'`|;&<>()]*)?')
HOME_PREFIXES = ("$env:USERPROFILE", "${HOME}", "$HOME", "%USERPROFILE%")
GENEGEERD = ("/dev/",)  # /dev/null en dergelijke zijn geen bestanden van de gebruiker


def norm(p, base, home):
    """Maak van een pad uit de invoer een absoluut, genormaliseerd pad."""
    p = p.strip().strip('"').strip("'")
    for pre in HOME_PREFIXES:
        if p.lower().startswith(pre.lower()):
            p = home + p[len(pre):]
            break
    if p == "~" or p.startswith("~/") or p.startswith("~\\"):
        p = home + p[1:]
    if os.name == "nt":
        m = re.match(r"^/([A-Za-z])(/|$)", p)  # Git Bash: /c/Users -> c:/Users
        if m:
            p = m.group(1) + ":/" + p[3:]
    if not os.path.isabs(p):
        p = os.path.join(base, p)
    return os.path.normcase(os.path.realpath(p))


def inside(p, root):
    try:
        return os.path.commonpath([p, root]) == root
    except ValueError:  # ander station
        return False


def settings_dirs(project, home):
    """additionalDirectories uit de instellingen van de gebruiker en het project."""
    files = [os.path.join(home, ".claude", "settings.json"),
             os.path.join(home, ".claude", "settings.local.json"),
             os.path.join(project, ".claude", "settings.json"),
             os.path.join(project, ".claude", "settings.local.json")]
    out = []
    for f in files:
        try:
            with open(f, encoding="utf-8") as fh:
                out += json.load(fh).get("permissions", {}).get("additionalDirectories", []) or []
        except (OSError, ValueError, AttributeError):
            pass
    return out


def uitzonderingen(project):
    """De toegestane mappen van dit project, uit .claude/toegestane-mappen.txt."""
    try:
        with open(os.path.join(project, UITZONDERINGEN), encoding="utf-8") as fh:
            return [l.strip() for l in fh if l.strip() and not l.strip().startswith("#")]
    except OSError:
        return []


def shell_candidates(cmd):
    cands = []

    def scan(text, depth):
        for m in QUOTED.finditer(text):
            inner = m.group(1) if m.group(1) is not None else m.group(2)
            if ABS_START.match(inner) and "\n" not in inner and len(inner) < 400:
                cands.append(inner)
            elif depth < 2:
                scan(inner, depth + 1)
        rest = QUOTED.sub(" ", text)
        cands.extend(EMBEDDED.findall(rest))
        cands.extend(HOMEISH.findall(rest))
        cands.extend(PARENT.findall(rest))

    scan(cmd, 0)
    return [c for c in cands if not c.startswith(GENEGEERD)]


def buiten_paden(data, env, home, extra_roots=()):
    """Geef de paden uit de invoer die buiten alle toegestane mappen vallen."""
    tool = data.get("tool_name", "")
    inp = data.get("tool_input") or {}
    cwd = data.get("cwd") or os.getcwd()
    project = env.get("CLAUDE_PROJECT_DIR") or cwd

    if tool == "Read":
        cands = [inp.get("file_path", "")]
    elif tool in ("Grep", "Glob"):
        cands = [inp.get("path") or cwd]
        pat = inp.get("pattern", "")
        if tool == "Glob" and ABS_START.match(pat):
            cands.append(re.split(r"[*?\[{]", pat, maxsplit=1)[0])
    elif tool in ("Bash", "PowerShell"):
        cands = shell_candidates(inp.get("command", ""))
    else:
        return []
    cands = [c for c in cands if c]
    if not cands:
        return []

    roots = [project, os.path.join(home, ".claude")]
    roots += [env.get(k, "") for k in ("TEMP", "TMP", "TMPDIR")] + list(extra_roots)
    roots += settings_dirs(project, home) + uitzonderingen(project)
    genormaliseerd = set()
    for r in roots:
        if r:
            try:
                genormaliseerd.add(norm(r, project, home))
            except (OSError, ValueError):
                pass

    buiten = []
    for c in cands:
        try:
            p = norm(c, cwd, home)
        except (OSError, ValueError):
            continue
        if not any(inside(p, r) for r in genormaliseerd) and p not in buiten:
            buiten.append(p)
    return buiten


def antwoord(buiten):
    lijst = "; ".join(buiten[:3]) + (" …" if len(buiten) > 3 else "")
    return {"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": BESLISSING,
        "permissionDecisionReason": (
            f"Buiten de projectmap: {lijst}. Sta dit alleen toe als je hier zelf om hebt gevraagd. "
            f"Vaste uitzondering voor dit project? Zet de map in {UITZONDERINGEN} "
            f"en leg de keuze vast in docs/decisions.md."),
    }}


def main():
    data = json.load(sys.stdin)
    buiten = buiten_paden(data, os.environ, os.path.expanduser("~"), [tempfile.gettempdir()])
    if buiten:
        print(json.dumps(antwoord(buiten), ensure_ascii=False))


def zelftest():
    import shutil
    import subprocess

    basis = tempfile.mkdtemp(prefix="projectmap-zelftest-")
    try:
        project = os.path.join(basis, "project")
        home = os.path.join(basis, "home")
        elders = os.path.join(basis, "elders")
        toegestaan = os.path.join(basis, "toegestaan")
        extra = os.path.join(basis, "extra")
        tijdelijk = os.path.join(basis, "tijdelijk")
        src = os.path.join(project, "src")
        for d in (os.path.join(project, ".claude"), src, os.path.join(home, ".claude"),
                  elders, toegestaan, extra, tijdelijk):
            os.makedirs(d, exist_ok=True)
        with open(os.path.join(project, UITZONDERINGEN), "w", encoding="utf-8") as f:
            f.write("# Toegestaan na akkoord, zie docs/decisions.md\n" + toegestaan + "\n")
        with open(os.path.join(project, ".claude", "settings.json"), "w", encoding="utf-8") as f:
            json.dump({"permissions": {"additionalDirectories": [extra]}}, f)
        env = {"CLAUDE_PROJECT_DIR": project, "TEMP": tijdelijk}

        def geval(tool, invoer, cwd=project):
            return {"tool_name": tool, "tool_input": invoer, "cwd": cwd}

        def sh(c, cwd=project):
            return geval("Bash", {"command": c}, cwd)

        def ps(c):
            return geval("PowerShell", {"command": c})

        slash = lambda p: p.replace("\\", "/")
        gevallen = [
            ("Read in de projectmap", geval("Read", {"file_path": os.path.join(project, "README.md")}), False),
            ("Read buiten de projectmap", geval("Read", {"file_path": os.path.join(elders, "x.txt")}), True),
            ("Read via ..", geval("Read", {"file_path": os.path.join(project, "..", "elders", "x.txt")}), True),
            ("Read in ~/.claude", geval("Read", {"file_path": os.path.join(home, ".claude", "settings.json")}), False),
            ("Read in de tijdelijke map", geval("Read", {"file_path": os.path.join(tijdelijk, "a.txt")}), False),
            ("Read in een toegestane map", geval("Read", {"file_path": os.path.join(toegestaan, "a.docx")}), False),
            ("Read in additionalDirectories", geval("Read", {"file_path": os.path.join(extra, "a.txt")}), False),
            ("Read zonder pad", geval("Read", {}), False),
            ("Grep zonder pad", geval("Grep", {"pattern": "x"}), False),
            ("Grep buiten", geval("Grep", {"pattern": "x", "path": elders}), True),
            ("Glob relatief", geval("Glob", {"pattern": "**/*.md"}), False),
            ("Glob met absoluut patroon buiten", geval("Glob", {"pattern": slash(elders) + "/**/*.md"}), True),
            ("Bash zonder paden", sh("git status && ls src"), False),
            ("Bash met Git-ref en sed", sh("git log origin/main && sed -i s/a/b/ src/x.py"), False),
            ("Bash met URL", sh("curl -s https://example.com/home/x/c/d"), False),
            ("Bash met /dev/null", sh("ls src 2>/dev/null"), False),
            ("Bash met pad in de projectmap", sh('ls "' + slash(project) + '/src"'), False),
            ("Bash met pad buiten tussen aanhalingstekens", sh('cat "' + slash(elders) + '/x.txt"'), True),
            ("Bash naar de bovenliggende map", sh("ls .."), True),
            ("Bash vanuit submap naar ../", sh("ls ../.claude", cwd=src), False),
            ("Bash naar de thuismap", sh("ls ~"), True),
            ("Bash naar ~/.claude", sh("cat ~/.claude/settings.json"), False),
            ("Bash met POSIX-thuispad", sh("cat /home/iemand/notities.txt"), True),
            ("Bash met Git Bash-pad", sh("ls /c/Windows/system32"), True),
            ("PowerShell met USERPROFILE", ps("Get-ChildItem $env:USERPROFILE\\Documents"), True),
            ("Ander gereedschap", geval("Write", {"file_path": os.path.join(elders, "x.txt")}), False),
        ]
        if os.name == "nt":
            gevallen.append(("PowerShell met Windows-pad", ps("Get-Content C:\\Windows\\win.ini"), True))

        fouten = 0
        for naam, data, verwacht in gevallen:
            uitkomst = bool(buiten_paden(data, env, home, [tijdelijk]))
            ok = uitkomst == verwacht
            fouten += not ok
            print(("OK   " if ok else "FOUT ") + naam + ("" if ok else f" (verwacht {verwacht}, kreeg {uitkomst})"))

        # Aanroep zoals Claude Code die doet: JSON via stdin, antwoord via stdout.
        omgeving = dict(os.environ, CLAUDE_PROJECT_DIR=project, HOME=home, USERPROFILE=home,
                        TEMP=tijdelijk, TMP=tijdelijk, TMPDIR=tijdelijk)
        for naam, data, verwacht in [
            ("stdin: Read buiten geeft een vraag", geval("Read", {"file_path": os.path.join(elders, "x.txt")}), True),
            ("stdin: Read binnen blijft stil", geval("Read", {"file_path": os.path.join(project, "a.txt")}), False),
            ("stdin: kapotte invoer blokkeert niet", None, False),
        ]:
            invoer = "{kapot" if data is None else json.dumps(data)
            r = subprocess.run([sys.executable, "-I", os.path.abspath(__file__)], input=invoer,
                               capture_output=True, text=True, env=omgeving, timeout=30)
            vraag = False
            if r.stdout.strip():
                vraag = json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"] == BESLISSING
            ok = r.returncode == 0 and vraag == verwacht
            fouten += not ok
            print(("OK   " if ok else "FOUT ") + naam + ("" if ok else f" (exit {r.returncode}, uitvoer {r.stdout!r})"))

        totaal = len(gevallen) + 3
        print(f"\n{totaal - fouten} van {totaal} gevallen geslaagd.")
        return 1 if fouten else 0
    finally:
        shutil.rmtree(basis, ignore_errors=True)


if __name__ == "__main__":
    if "--zelftest" in sys.argv:
        sys.exit(zelftest())
    try:
        main()
    except Exception:  # een fout in de hook mag het werk niet blokkeren
        pass
