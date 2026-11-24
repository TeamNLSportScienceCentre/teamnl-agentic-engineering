---
titel: "Hooks: de agent technisch tegenhouden"
categorie: wat-mag-hij
moeilijkheid: 2
---

# Hooks: de agent technisch tegenhouden

## In één zin
Een hook is een kleine, automatische controle die meekijkt vóórdat je agent iets doet, en de actie tegenhoudt als die niet mag.

## Waarom
Een afspraak in [`AGENTS.md`](../repo/agents-md.md) ("open `data/private/` niet") is een bordje: de agent leest het en houdt zich er meestal aan, maar het blijft een verzoek. Een hook is een slagboom: hij controleert elke actie waarvoor je hem instelt. Zo blijft je brondata dicht, ook als de agent zich vergist of jij even niet oplet bij het goedkeuren.

## Wanneer wel, wanneer (nog) niet
- **Wel:** je project heeft data die de agent niet mag zien (atleetdata, data van een externe partij), en je wilt dat niet alleen afspreken maar ook afdwingen.
- **Nog niet:** je werkt alleen met nepdata. Begin dan met een goede scheiding van [data folders](../repo/data-folders.md).
- Een hook vervangt geen toestemming van de data-eigenaar. Mag de data helemaal niet in de buurt van een AI-aanbieder, zet hem dan ook buiten je projectmap.

## Zo begin je
Je hoeft het script niet zelf te schrijven. Vraag je agent:
> *"Stel voor dit project een hook in die voorkomt dat je bestanden in `data/private/` opent. Laat eerst zien wat je gaat aanpassen."*

Bij Claude Code ziet dat er ongeveer zo uit. `.claude/settings.json` zet de hook aan:
```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Read|Edit|Write|Bash",
        "hooks": [ { "type": "command", "command": "python scripts/hooks/check_toegang.py" } ] }
    ]
  }
}
```
`scripts/hooks/check_toegang.py` doet de controle. De agent geeft de geplande actie als JSON door; exitcode 2 houdt de actie tegen en de tekst op stderr hoort de agent als uitleg:
```python
import json, sys
actie = json.dumps(json.load(sys.stdin).get("tool_input", {}))
if "data/private" in actie.replace("\\\\", "/"):
    print("Geblokkeerd: data/private/ is afgeschermd voor de agent.", file=sys.stderr)
    sys.exit(2)
```
**Test hem altijd:** vraag de agent een nepbestand in `data/private/` te openen en kijk naar de melding van de hook zelf, niet alleen naar wat de agent zegt.

Codex en GitHub Copilot in VS Code hebben vergelijkbare hooks met een eigen plek en eigen namen. Het idee is hetzelfde; controleer de actuele documentatie van jouw agent.

## Valkuilen
- **Een hook controleert alleen wat je hem laat controleren.** Een agent die een Python-script schrijft dat het bestand alsnog opent, of een pad anders schrijft, kan langs een simpele tekstcontrole. Combineer hooks met [deny-regels](permissies-en-guardrails.md) en, voor echt gevoelige data, een [sandbox](sandbox.md) of data buiten de projectmap.
- Een agenthook is iets anders dan een Git-hook ([pre-commit](../repo/gitleaks-pre-commit.md)): die kijkt pas mee bij een commit.
- Hooks staan in de repo en draaien op je eigen computer. Lees een hook van een ander voordat je hem aanzet.
- Kun je deze drie zinnen invullen? *Dit mag mijn agent gebruiken. Hier staat mijn hook. Zo heb ik getest dat hij werkt.*

## Zie ook
[`permissies-en-guardrails.md`](permissies-en-guardrails.md) · [`data-access.md`](data-access.md) · [`sandbox.md`](sandbox.md) · [`../repo/data-folders.md`](../repo/data-folders.md)
