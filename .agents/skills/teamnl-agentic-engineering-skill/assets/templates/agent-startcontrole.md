# Agents starten en controleren

Start de agent altijd vanuit de root van deze repository. De map die je opent,
is de wereld van de agent. Commando's met `$` of `/` typ je in het gesprek met
de agent, niet in een terminal.

| Agent | Starten | Skill aanroepen | Let op |
| --- | --- | --- | --- |
| Codex (CLI of VS Code) | `codex` | `$teamnl-agentic-engineering-skill` | Projectconfiguratie en hooks laden alleen in een vertrouwd project. Herstart Codex als een nieuwe skill niet verschijnt. |
| Claude Code (CLI of VS Code) | `claude` | `/teamnl-agentic-engineering-skill` | Skill via `.claude/skills/`. Op Windows werkt `claude.cmd` als PowerShell de `.ps1`-starter blokkeert. Wijzig daarvoor geen systeembeleid. |
| GitHub Copilot (VS Code of CLI) | Chat in agentmodus, of `copilot` | `/teamnl-agentic-engineering-skill` | Skill via `.agents/skills/`. |
| Mistral Vibe | `vibe` | `/teamnl-agentic-engineering-skill` | Laadt projectskills, `AGENTS.md` en projectconfiguratie alleen in een vertrouwde map. Controleer de inhoud voordat je de map vertrouwt. |

Hoe de skill per agent wordt gevonden en welke instellingen er zijn, staat in
`.agents/skills/teamnl-agentic-engineering-skill/references/agent-inrichting.md`.

## Geteste status in dit project

Vul dit in na een echte controle in deze omgeving. 'Niet getest' betekent dat de
werking alleen uit de documentatie volgt.

| Agent en versie | Besturingssysteem | Skill zichtbaar | AGENTS.md gelezen | Keuzeknoppen | Datum | Opmerkingen |
| --- | --- | --- | --- | --- | --- | --- |
| Codex | | niet getest | niet getest | niet getest | | |
| Claude Code | | niet getest | niet getest | niet getest | | |
| GitHub Copilot | | niet getest | niet getest | niet getest | | |
| Mistral Vibe | | niet getest | niet getest | niet getest | | |

## Toegangsgrenzen

Test met fictieve proefbestanden, volgens de procedure in `agent-inrichting.md`.
Welke tests verplicht zijn, hangt af van het risiconiveau in `AGENTS.md`.

| Agent en versie | Inrichting (bestand) | 1. Direct lezen geblokkeerd | 2. Via opdracht geblokkeerd | 3. Alleen samenvatting terug | 4. Geen lek via uitvoer, logs of bestanden | 5. Hook ontbreekt of faalt | Datum |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code | `.claude/settings.json` | niet getest | niet getest | niet getest | niet getest | n.v.t. (geen hook) | |
| Codex | `.codex/hooks.json` (bij risiconiveau hoog) | niet getest | niet getest | niet getest | niet getest | n.v.t. (geen hook) | |
| GitHub Copilot | `.github/hooks/` (bij risiconiveau hoog) | niet getest | niet getest | niet getest | niet getest | n.v.t. (geen hook) | |
| Mistral Vibe | `.vibe/hooks.toml` (bij risiconiveau hoog) | niet getest | niet getest | niet getest | niet getest | n.v.t. (geen hook) | |

Een route die niet wordt geblokkeerd, is een beperking. Noteer die hier en in
`AGENTS.md`. Maak echte data dan niet toch toegankelijk.

## Projectmap-hook (Claude Code)

Zie de procedure in `agent-inrichting.md`, onder Projectmap-hook.

| Claude Code-versie | Zelftest geslaagd | Lezen buiten de projectmap geeft een vraag | Lezen binnen de projectmap gaat door | Uitzondering in `.claude/toegestane-mappen.txt` werkt | Datum |
| --- | --- | --- | --- | --- | --- |
| | niet getest | niet getest | niet getest | niet getest | |

## Controle op secrets vóór een commit

| Computer of gebruiker | `pre-commit install` uitgevoerd | Test met een nep-secret geblokkeerd | Datum |
| --- | --- | --- | --- |
| | niet getest | niet getest | |
