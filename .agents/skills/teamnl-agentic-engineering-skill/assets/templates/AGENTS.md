# AGENTS.md

Werkafspraken voor coding agents in dit project. Dit bestand is kort en verwijst
naar de details. Uitleg voor mensen staat in `README.md`.

## Project

- Status: nog niet ingericht. Stel voor om eerst de teamnl-agentic-engineering-skill te starten (route Nieuw project), voordat je iets bouwt.
- Doel: nog niet vastgelegd.
- Actief plan: nog geen.
- TeamNL-basis: standaardrepo 1.3.0 (teamnl-agentic-engineering-skill 2.3.0).
- Voorbeelden: bestanden met `status: voorbeeld` of met `voorbeeld` in de naam komen uit de basis. Ze laten het format zien en zijn geen projectbestanden of actieve plannen.

## Bij elke nieuwe sessie eerst lezen

1. Dit bestand en het actieve plan hierboven.
2. De nieuwste handoff in `docs/handoffs/`.
3. `docs/decisions.md`, voor de goedgekeurde keuzes.

## Data access

- Data-eigenaar/bevoegde rol: nog niet vastgelegd. Tot dat is vastgelegd: alleen fictieve data.
- Agent mag niet lezen, printen of uploaden: `.env` en varianten (behalve `.env.example` met fictieve waarden), `data/private/`, `media/private/`.
- Ontwikkel en test met fictieve data in `data/example/`, elk bestand < 1 MB.
- Uitvoer naar de agent: alleen niet-herleidbare samenvattingen. Geen echte rijen, secrets of waarden in foutmeldingen, logs, notebooks of exports.
- Technische toegangsregels: `.claude/settings.json` (Claude Code), met de leesblokkades en de projectmap-hook `.agents/hooks/buiten-projectmap.py`. De geteste status per agent staat in `docs/agent-startcontrole.md`. Instructies alleen zijn geen technische blokkade.
- Mappen buiten de projectmap: niet lezen. De projectmap-hook vraagt dan om toestemming. Vaste uitzonderingen alleen na akkoord, in `.claude/toegestane-mappen.txt` (buiten Git) en in `docs/decisions.md`.
- Verruim deze grenzen nooit stilzwijgend. Stel een wijziging zichtbaar voor en leg die na akkoord hier en in `docs/decisions.md` vast.

## Werkwijze

- Werk vanuit het actieve plan, in kleine stappen. Stop bij de afgesproken controlemomenten.
- Nieuw werk krijgt een eigen plan via de skill: een feature in `specs/<feature>/`, een repo-update in `docs/repo-updates/<moment>/`.
- Installeer of wijzig niets buiten deze repository zonder eerst te tonen wat er gebeurt en akkoord te krijgen.
- Git-werkwijze: nog niet vastgelegd. Commit of push alleen als de gebruiker daarom vraagt. Sla de controle op secrets vóór een commit nooit over.
- Leg goedgekeurde keuzes met hun reden vast in `docs/decisions.md`.
- Sluit elke werksessie af met een geschoonde handoff in `docs/handoffs/YYYY-MM-DD-HHMM-onderwerp.md`.

## Starten, testen en controleren

- Installeren en starten: nog niet vastgelegd (zie `README.md`).
- Automatische tests: nog niet vastgelegd.

## Namen en mappen

- Eigen bestanden en mappen: kleine letters met streepjes. Python-modules: underscores.
- Vaste namen blijven: `AGENTS.md`, `CLAUDE.md`, `README.md`, `SKILL.md`.
- Ruwe logs staan in `logs/runtime/` en `logs/test/`, buiten Git.
- Standaardindeling en uitbreidingen: `.agents/skills/teamnl-agentic-engineering-skill/references/standaardrepo.md`.

## TeamNL-basis

- De skillmap `.agents/skills/teamnl-agentic-engineering-skill/` en de ingangen per agent horen bij de basis. Pas die in dit project niet aan. Projectafspraken staan hier en in `docs/`.
- TeamNL-afspraken gaan voor op afwijkende defaults uit andere skills.
