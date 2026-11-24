# De TeamNL-standaardrepo

Dit bestand beschrijft de indeling van de basisrepo en de afspraken over namen en
locaties. Het schrijft geen programmeertaal of framework voor.

De basisrepo bevat de volledige indeling als **geraamte**. Elke standaardmap is
zichtbaar, met een korte README en waar het zinvol is een voorbeeldbestand. Zo
ziet een deelnemer direct welke keuzes er zijn. Een project houdt alleen wat het
nodig heeft. Bij de inrichting stelt de skill in het plan voor welke mappen
blijven en welke weg kunnen. In bestaande projecten blijven werkende paden en
eerdere plannen behouden, tenzij een wijziging expliciet wordt afgesproken. Daar
voeg je alleen gericht toe wat ontbreekt.

## Vaste kern: blijft in elk project

| Bestand of locatie | Functie | Sjabloon in `assets/templates/` |
| --- | --- | --- |
| `README.md` | Uitleg voor mensen: doel, installatie, starten, gebruiken, controleren en benodigde toegang | `README.md`. De root-README van de basis wordt vervangen. |
| `AGENTS.md` | Compacte projectafspraken, met verwijzingen naar het actieve plan, de beslissingen, de data-afspraken en de handoffs | `AGENTS.md` |
| `CLAUDE.md` | Ingang voor Claude Code: importeert `AGENTS.md` | `CLAUDE.md` |
| `.gitignore` | Git-uitsluitingen; geen toegangsregeling voor de agent | `gitignore.txt` |
| `.gitattributes` | Regeleindes en binaire bestanden | `gitattributes.txt` |
| `.pre-commit-config.yaml` | Gitleaks-controle op secrets vóór een commit | `pre-commit-config.yaml` |
| `.claude/settings.json` | Standaard leesblokkades en de projectmap-hook voor Claude Code | `claude-settings.json` |
| `.agents/hooks/buiten-projectmap.py` | Projectmap-hook: vraagt om toestemming bij lezen buiten de projectmap, zie [agent-inrichting.md](agent-inrichting.md#projectmap-hook-claude-code) | `buiten-projectmap.py` |
| `.agents/skills/teamnl-agentic-engineering-skill/` | Deze skill: de centrale instructies, referenties en sjablonen | n.v.t. |
| Ingangen per agent | Verwijzingen naar dezelfde skill, zie [agent-inrichting.md](agent-inrichting.md) | n.v.t. |
| `docs/decisions.md` | Goedgekeurde keuzes met hun reden | `decisions.md` |
| `docs/handoffs/` | Beknopte, geschoonde verslagen per werksessie | `handoffs-README.md` en `handoff.md` |
| `docs/agent-startcontrole.md` | Starten per agent en de geteste status van ingangen en toegangsregels | `agent-startcontrole.md` |
| `logs/` met `runtime/` en `test/` | Afspraken over logs; ruwe logs buiten Git | `logs-README.md` |

## Geraamte: aanwezig in de basis, het project kiest

| Locatie | Functie | Blijft als |
| --- | --- | --- |
| `docs/project/` | Plan voor de start van het project: `plan-van-aanpak.md` | Altijd |
| `specs/<feature>/` | Eigen plan per feature, met meerdere kleine bouwstappen | Altijd, zodra er features komen |
| `docs/repo-updates/<YYYY-MM-DD-onderwerp>/` | Eigen plan per opdracht om de repo aan te vullen of bij te werken | Altijd |
| `docs/architecture.md` | Actuele uitleg van de architectuur | De opbouw uitleg nodig heeft |
| `docs/data-afspraken.md` | Details per bron als het blok in `AGENTS.md` te groot wordt | Er meerdere bronnen of uitgebreide afspraken zijn |
| `docs/bronnen/` | Bronverwijzingen en toegestane technische documentatie | Er externe bronnen zijn |
| `src/` | Broncode; de indeling volgt uit het project | Er code is |
| `tests/` met `fixtures/` | Passende automatische tests en kleine, fictieve testbestanden | Er code is |
| `data/` met `example/` en `private/` | Fictieve voorbeelden in Git (< 1 MB per bestand); echte data buiten Git | Het project met data werkt |
| `media/` met `example/` en `private/` | Deelbare voorbeeldmedia met gebruiksrecht; vertrouwelijke media buiten Git | Er beeld, video of geluid is |
| `scripts/` | Projectgebonden hulpscripts | Er hulpscripts zijn |
| `install.cmd`, `install.ps1` en `install.sh` | Installatieroute met overzicht en toestemming, zie [installatie.md](installatie.md) | Het programma geïnstalleerd moet worden. Houd alleen de systemen die de gebruikers echt gebruiken. |
| `.env.example` | Deelbaar configuratievoorbeeld zonder echte waarden | Het project configuratie of secrets nodig heeft |
| `design.md` | De vastgelegde TeamNL-stijl, zie [teamnl-stijl.md](teamnl-stijl.md) | Er een gebruikersinterface is |
| `assets/brand/` | Geverifieerde huisstijlassets | Er een gebruikersinterface is |
| `output/` | Gegenereerde resultaten, standaard buiten Git | Het project bestanden genereert |
| `tmp/` | Tijdelijke bestanden, buiten Git | Het project tijdelijke bestanden maakt |
| `archive/` | Eerder werk als referentie, niet als fundament; alleen deelbare code | Er eerder werk is |
| `server/` | Afzonderlijke backendservice | Er een aparte backend is |
| `database/` met `migrations/` | Schema en migraties, geen data | Er een database is |
| `.github/workflows/` | Automatische controles of deployment | Die nodig zijn |

Elke map heeft een korte README met drie onderdelen: wat erin hoort, of het in
Git staat en wanneer je de map weghaalt. Maak je zo'n map in een bestaand project?
Gebruik dan dezelfde opzet. De README's in de basisrepo zijn het voorbeeld. Een
map waarvan de inhoud buiten Git blijft, zoals `data/private/`, houdt een
`.gitkeep` met één regel uitleg.

Er is één vaste locatie per soort bestand. Voeg geen concurrerende bronmappen
toe. Een genegeerde map is op zichzelf geen beveiliging. Bij gevoelige data
bepaalt goedgekeurde opslag waar die thuishoort, eventueel buiten de repo.

## Voorbeeldbestanden in de basis

Deze bestanden horen bij één fictieve casus: een trainingsbelastingdashboard voor
het verzonnen schaatsteam 'Team Voorbeeld'. Ze laten het format zien. Het zijn
geen projectbestanden of actieve plannen. Een voorbeeldplan herken je aan
`status: voorbeeld`. Een voorbeeldbestand of -map heeft `voorbeeld` in de naam.

| Voorbeeld | Laat zien |
| --- | --- |
| `docs/project/voorbeeld-plan-van-aanpak.md` | Een kort plan voor een nieuw project |
| `specs/voorbeeld-weekexport/` | Een kort featureplan |
| `docs/repo-updates/2026-11-17-voorbeeld-agent-ready/` | Een kort plan voor een repo-update |
| `data/example/voorbeeld-trainingen.csv` | Fictieve voorbeelddata, beschreven in `data/README.md` |
| `tests/fixtures/voorbeeld-invoer.csv` | Een testbestand met opzettelijke fouten |
| `media/example/voorbeeld-afbeelding.svg` | Een voorbeeldmedium (placeholder, geen logo) |

Bij de inrichting van een nieuw project verwijder je deze voorbeelden. Je kunt
ze ook vervangen door echte projectbestanden. Pas daarbij de tabel in
`data/README.md` aan.

## Namen

- Eigen documenten en mappen: kleine letters met streepjes, bijvoorbeeld
  `plan-van-aanpak.md`.
- Vaste herkenningsnamen blijven behouden: `AGENTS.md`, `CLAUDE.md`,
  `README.md` en `SKILL.md`.
- Python-modules gebruiken underscores, omdat Python geen streepjes kan
  importeren.
- Handoffs: `YYYY-MM-DD-HHMM-onderwerp.md`.
- Repositories: `doelgroep-doel-specifiek`, bijvoorbeeld
  `knzb-belasting-monitor`.
- Branches, als de gebruiker die gebruikt: `soort/onderwerp`, bijvoorbeeld
  `feature/sprint-export`.
- Geen spaties, en geen 'final', 'nieuw' of 'v2' in namen. Daarvoor is Git.

Gebruik `docs/decisions.md` en `docs/architecture.md` in kleine letters. Het
naslagwerk noemt elders `DECISIONS.md`. Volg in een bestaand project de naam
die al wordt gebruikt.

## Basis voor .gitignore

Het sjabloon `assets/templates/gitignore.txt` bevat de basis. Een genegeerde map
die zichtbaar moet blijven, staat erin als `map/*` met de uitzondering
`!map/.gitkeep`.

- **Aanvullen per stack.** Vul de basis aan voor de gekozen stack, bijvoorbeeld
  met `.venv/` en `__pycache__/` bij Python of met `node_modules/` bij JavaScript.
- **Bestanden die Git al volgt.** Die worden niet vanzelf genegeerd. Controleer
  dat met `git ls-files` en `git check-ignore -v <pad>`.
- **Secret in de geschiedenis.** Verwijderen is dan niet genoeg: vervang het
  secret.

## Wat hoort bij de basis en wat bij het project

Dit onderscheid maakt een update van de basis mogelijk zonder dat projectafspraken
verloren gaan.

| Van de basis: bij een update vervangen na akkoord | Van het project: alleen gerichte verbeteringen na akkoord |
| --- | --- |
| `.agents/skills/teamnl-agentic-engineering-skill/` | `AGENTS.md` (behalve de regel `TeamNL-basis:`) |
| De ingangen per agent die naar de skill verwijzen | `README.md` en de README's per map |
| | `.gitignore`, `.gitattributes`, `.pre-commit-config.yaml`, `.claude/settings.json` en `.agents/hooks/buiten-projectmap.py` (vergelijk met de sjablonen). Bij risiconiveau hoog ook de rest van `.agents/hooks/`, `.codex/`, `.github/hooks/`, `.vibe/` en `.gitleaks.toml`; die past de gebruiker zelf aan. |
| | `.claude/toegestane-mappen.txt`, buiten Git |
| | Plannen, `docs/decisions.md`, handoffs, `design.md`, de installatiescripts en de data-afspraken |
| | Alle code, tests en data |

Pas in een project niets aan in de skillmap. Een projectspecifieke afspraak
hoort in `AGENTS.md` of `docs/`.

## Basisversie

`AGENTS.md` bevat een regel als deze:

```text
- TeamNL-basis: standaardrepo 1.3.0 (teamnl-agentic-engineering-skill 2.3.0), overgenomen op YYYY-MM-DD.
```

De versiegeschiedenis staat in de `CHANGELOG.md` van de skill.

## Kern overnemen buiten de basisrepo

Begint een nieuw project in een map zonder basis, leeg of met een paar eigen
bestanden? Of mist een bestaande repo de kern?
Neem dan na goedkeuring van het plan de sjablonen over uit `assets/templates/`.
Neem van het geraamte alleen de mappen die het project nodig heeft.

| Sjabloon | Doel in het project |
| --- | --- |
| `AGENTS.md` | `AGENTS.md`, daarna invullen |
| `CLAUDE.md` | `CLAUDE.md` |
| `README.md` | `README.md`, daarna invullen |
| `gitignore.txt` | `.gitignore`, samenvoegen met een bestaande |
| `gitattributes.txt` | `.gitattributes`, samenvoegen met een bestaande |
| `pre-commit-config.yaml` | `.pre-commit-config.yaml` |
| `claude-settings.json` | `.claude/settings.json`, samenvoegen met bestaande instellingen |
| `buiten-projectmap.py` | `.agents/hooks/buiten-projectmap.py` |
| `decisions.md` | `docs/decisions.md` |
| `handoffs-README.md` | `docs/handoffs/README.md` |
| `logs-README.md` | `logs/README.md` |
| `agent-startcontrole.md` | `docs/agent-startcontrole.md` |
| `architecture.md` en `data-afspraken.md` | `docs/`, alleen als dat nodig is |
| `data-README.md` | `data/README.md`, als het project met data werkt |
| `env.example` | `.env.example`, als configuratie nodig is |
| `design.md` | `design.md`, bij een gebruikersinterface |
| `install/` | `install.cmd`, `install.ps1` en `install.sh`, als installatie nodig is |

Kopieer daarnaast de skillmap en de ingangen per agent. Voeg een bestaand
bestand altijd samen met het sjabloon. Overschrijf het nooit, en laat het
verschil zien.

## Uitbreiding bij risiconiveau hoog

Deze bestanden staan niet in de basis. Een project krijgt ze alleen bij
[risiconiveau](data-afspraken.md#risiconiveau) hoog. Hoe je ze inricht, staat in
[agent-inrichting.md](agent-inrichting.md#bescherming-bij-risiconiveau-hoog).

| Sjabloon in `assets/templates/hoog-risico/` | Doel in het project |
| --- | --- |
| `bescherm-gevoelige-data.py` | `.agents/hooks/bescherm-gevoelige-data.py` |
| `claude-settings.json` | `.claude/settings.json`, samengevoegd met bestaande instellingen |
| `codex-hooks.json` | `.codex/hooks.json` |
| `copilot-hooks.json` | `.github/hooks/teamnl-bescherming.json` |
| `vibe-hooks.toml` | `.vibe/hooks.toml` |
| `gitleaks.toml` | `.gitleaks.toml` |
