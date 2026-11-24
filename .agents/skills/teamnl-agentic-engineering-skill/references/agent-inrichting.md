# Inrichting per agent

De inhoudelijke afspraken staan op één plek: `AGENTS.md` en deze skill. Per
agent komen alleen de ingangen en de configuratie die nodig zijn. Claim pas dat
een agent wordt ondersteund nadat je dat hebt gecontroleerd in die agent en die
versie. Leg de uitkomst vast in `docs/agent-startcontrole.md`.

De feiten hieronder komen uit de officiële documentatie, geraadpleegd op
17 november 2026. De hooks van alle vier de agents en de padregels van Claude
Code zijn op 18 november 2026 nagelopen. In de praktijk zijn ze nog niet getest. Agents veranderen
snel: controleer de documentatie bij twijfel opnieuw.

## Ingangen en instructies

| Agent | Skill gevonden in | Leest instructies uit | Aanroepen |
| --- | --- | --- | --- |
| Codex (CLI en IDE) | `.agents/skills/` | `AGENTS.md` | `$teamnl-agentic-engineering-skill` |
| Claude Code | `.claude/skills/`, niet in `.agents/skills/` | `CLAUDE.md`, dat met `@AGENTS.md` `AGENTS.md` importeert | `/teamnl-agentic-engineering-skill` |
| GitHub Copilot (VS Code, CLI, cloudagent) | `.github/skills/`, `.claude/skills/` of `.agents/skills/` | VS Code: `AGENTS.md` en `.github/copilot-instructions.md`. CLI en cloudagent: daarnaast ook `CLAUDE.md` | `/teamnl-agentic-engineering-skill` |
| Mistral Vibe | `.agents/skills/` of `.vibe/skills/`, alleen in een vertrouwde map | `AGENTS.md` van de werkmap tot aan de root van de vertrouwde map | `/teamnl-agentic-engineering-skill` |

Daaruit volgt de inrichting van de basis:

- De skill staat in `.agents/skills/teamnl-agentic-engineering-skill/`. Codex,
  Copilot en Vibe lezen die map direct.
- `.claude/skills/teamnl-agentic-engineering-skill/SKILL.md` is alleen een
  verwijzing voor Claude Code, met dezelfde naam en beschrijving. Gebruik geen
  symlink, omdat Git op Windows die standaard niet aanmaakt.
- `CLAUDE.md` bevat `@AGENTS.md`. Recente versies van Claude Code lezen
  `AGENTS.md` ook zelf, maar alleen als er geen `CLAUDE.md` bestaat. De import
  werkt in alle versies.
- **Andere agents.** Gebruikt de deelnemer een andere agent? Controleer dan
  waar die skills en instructies zoekt. Voeg alleen een ingang toe die naar
  dezelfde centrale instructies verwijst. Herkent een agent geen skills? Dan
  kan de gebruiker het centrale instructiebestand als startdocument geven.

## Keuzetool per agent

| Agent | Tool | Bijzonderheden |
| --- | --- | --- |
| Claude Code | `AskUserQuestion` | Tot vier vragen per aanroep, twee tot vier opties, plus een vrij antwoord |
| Codex | `request_user_input` | Standaard alleen in planmodus. Hooguit drie vragen en twee à drie opties, plus een vrij antwoord. |
| GitHub Copilot | `ask_user` (CLI), `askQuestions` (VS Code) | Of `askQuestions` in elke VS Code-modus beschikbaar is, is niet gedocumenteerd |
| Mistral Vibe | `ask_user_question` | Eén tot vier vragen en twee tot vier opties, plus een vrij antwoord. Subagents kunnen geen vragen stellen. |

Is de tool niet beschikbaar, of meldt die een fout? Stel de vraag dan in tekst.
In de suggestiemodus zijn soms drie oplossingen en de optie Meer uitleg nodig.
Kan de agent maar drie opties tonen, zoals Codex? Laat dan Meer uitleg weg uit de
opties. Vermeld in de vraag dat de gebruiker in het vrije antwoord 'meer uitleg'
kan typen.

## Leesblokkades, instellingen en hooks

| Agent | Leesblokkade in de repo | Hooks | Gedrag bij een ontbrekende of falende hook |
| --- | --- | --- | --- |
| Claude Code | `.claude/settings.json` → `permissions.deny` met `Read(...)`, in gitignore-syntaxis. De regels gelden ook voor Grep, Glob en herkende shellcommando's zoals `cat` en `head`, maar niet voor scripts of `grep -r`. De sandbox maakt de blokkade op OS-niveau, maar werkt niet op native Windows. | `PreToolUse` en `PostToolUse` in `.claude/settings.json`. Exit 2 blokkeert. Uitvoer vervangen kan met `updatedToolOutput`. | Niet blokkerend, tenzij `"onFailure": "block"` is gezet (vanaf v2.1.295). |
| Codex | Permissieprofielen (bèta) met `deny` per pad in `.codex/config.toml`, voor commando's in de sandbox. Op native Windows beperkt, en genegeerd als ergens `sandbox_mode` staat. Zonder profiel kan Codex de hele schijf lezen. | `PreToolUse` en `PostToolUse` in `.codex/hooks.json`. Lezen gaat via `Bash`, wijzigen via `apply_patch`. Werkt alleen in een vertrouwd project, nadat de gebruiker de hook via `/hooks` heeft goedgekeurd. Na een wijziging van de configuratie staat de hook uit tot een nieuwe goedkeuring. | Laat door bij een crash, een time-out of een ontbrekende Python. Een fail-closed-optie is er niet. |
| GitHub Copilot | Geen leesblokkade met een repobestand. Content exclusion stel je in op GitHub (Business en Enterprise) en is geen beveiligingsgrens. | `preToolUse` en `postToolUse` in `.github/hooks/*.json`, voor de CLI, de cloudagent en VS Code (Copilot-harness, preview). De CLI en VS Code lezen ook de hooks in `.claude/settings.json`. Uitvoer vervangen kan met `modifiedResult`. | Een fout of crash blokkeert. Een time-out (standaard 30 s) laat de actie door. |
| Mistral Vibe | `denylist` per tool in `.vibe/config.toml`, voor de bestandstools maar niet voor `bash`. `sensitive_patterns` vraagt alleen om goedkeuring. | `pre_tool` en `post_tool` in `.vibe/hooks.toml`, alleen in een vertrouwde map en in de map waar je Vibe start. Weigeren gaat met JSON. Zoeken loopt via `bash`. | Alleen een waarschuwing, tenzij `strict = true` |

**Standaard in de basis.** De basis heeft `.claude/settings.json` met twee
onderdelen:

- leesblokkades voor `.env`-varianten, `data/private/` en `media/private/`;
- de projectmap-hook `.agents/hooks/buiten-projectmap.py`, zie
  [Projectmap-hook (Claude Code)](#projectmap-hook-claude-code).

Over de leesblokkades:

- **Uitzondering voor `.env.example`.** Die maak je met de `!`-regel. Werkt de
  uitzondering niet in een versie? Dan blijft `.env.example` ook geblokkeerd.
  Dat is veilig, maar wel onhandig.
- **Wat de leesblokkades niet dekken.** Ze gelden ook voor Grep, Glob en herkende
  shellcommando's zoals `cat`. Ze dekken niet `grep -r` vanuit een bovenliggende
  map, en ook geen scripts die zelf bestanden openen.
- **Risiconiveau hoog.** Dan komt de beschermhook erbij, zie
  [Bescherming bij risiconiveau hoog](#bescherming-bij-risiconiveau-hoog).

Voor Codex, Copilot en Vibe zit geen configuratie in de basis. Bij risiconiveau
hoog richt de uitvoeringsstap hun hooks in, zie hieronder.

Moet de agent echt niet bij data kunnen? Zet de data dan buiten de map waartoe
de agent toegang heeft. Een leesblokkade is geen kluis.

## Projectmap-hook (Claude Code)

Elk project krijgt de projectmap-hook, op elk risiconiveau. De hook staat in het
project en niet in de instellingen van de gebruiker (`~/.claude/settings.json`).
Zo geldt hij alleen in projecten waar hij is ingericht, en ziet iedereen in de
repo welke regel geldt.

**Wat de hook doet.** Leest of zoekt Claude Code buiten de projectmap? Dan vraagt
de hook eerst om toestemming. Hij controleert Read, Grep en Glob precies. In Bash-
en PowerShell-commando's zoekt hij naar paden voor Windows, Git Bash, macOS en
Linux, en naar de thuismap en `..`. Zonder vragen toegestaan zijn:

- de projectmap zelf;
- `~/.claude`, met de instellingen, het geheugen en de skills van de agent;
- de tijdelijke map;
- `permissions.additionalDirectories` uit de instellingen;
- de mappen in `.claude/toegestane-mappen.txt`.

| Bestand | Rol | Sjabloon |
| --- | --- | --- |
| `.agents/hooks/buiten-projectmap.py` | Het hookscript, met een zelftest | `buiten-projectmap.py` |
| `.claude/settings.json` | Roept de hook aan bij `PreToolUse` | `claude-settings.json` |
| `.claude/toegestane-mappen.txt` | Vaste uitzonderingen voor dit project: één pad per regel, `#` voor commentaar. Staat buiten Git, omdat paden per computer verschillen. | geen; maak het alleen aan als er een uitzondering is |

**Inrichten.** De hook zit in de basis. Mist een project hem, bijvoorbeeld bij de
route Bestaand? Neem dan beide sjablonen over, als onderdeel van de stap
Toegangsregels in het plan. Daarna:

1. **Python-commando controleren.** Het sjabloon gebruikt `python`. Werkt op
   macOS of Linux alleen `python3`? Pas het commando dan aan.
2. **Zelftest draaien:** `python .agents/hooks/buiten-projectmap.py --zelftest`.
3. **Activeren.** Claude Code neemt gewijzigde instellingen meestal direct over
   in de lopende sessie. Werkt de hook nog niet? Herstart dan de sessie.
4. **Globale versie opruimen.** Staat de projectmap-hook ook in
   `~/.claude/settings.json`? Stel dan voor die daar weg te halen, met de lijst
   `~/.claude/toegestane-mappen.txt`. Anders vraagt de hook twee keer, en geldt
   hij ook in projecten waar dat niet is afgesproken. Dit is een wijziging
   buiten de repo, dus pas na akkoord.

**Een uitzondering vastleggen.** Wijst de gebruiker een map buiten het project
aan die de agent vaker mag lezen, zoals een map met intakes of documentatie?

1. Vraag eerst akkoord. Een enkele leesactie kan ook via de toestemmingsvraag.
2. Zet het pad in `.claude/toegestane-mappen.txt`.
3. Leg de keuze met de reden vast in `docs/decisions.md`, zonder het volledige
   persoonlijke pad. Bijvoorbeeld: 'map met intakes op de teamsite'.

**Wat de hook niet tegenhoudt.**

- **Opgebouwde paden.** Een script dat zelf bestanden opent, of een pad uit een
  variabele, ziet de hook niet. Het is een vangnet tegen vergissingen, geen
  beveiligingsgrens. Voor gevoelige data gelden de leesblokkades en, bij hoog,
  de beschermhook.
- **Fouten.** Faalt de hook, of ontbreekt Python of het script? Dan gaat de
  actie door. Daarom eindigt het commando op `|| exit 0`. Zonder die toevoeging
  stopt Python bij een ontbrekend script met exitcode 2, en dan blokkeert Claude
  Code elke lees- en zoekactie. Haal `|| exit 0` dus niet weg.
- **Copilot.** Copilot leest ook de hooks in `.claude/settings.json`. Dat is
  niet getest. De toolnamen kunnen afwijken, en dan doet de hook niets. Of
  Copilot `CLAUDE_PROJECT_DIR` invult, is onbekend. Copilot weigert een actie als
  een hook faalt. Werkt het project met Copilot? Controleer dan dat gewone
  acties niet worden geweigerd.
- **Andere agents.** Codex en Vibe gebruiken deze hook niet. Daar begrenst de
  map waarin je de agent start wat hij ziet, zie de tabel hierboven.

## Bescherming bij risiconiveau hoog

Bij risiconiveau hoog richt je de sjablonen uit `assets/templates/hoog-risico/`
in. Dat doe je in de eerste bouwstap, na akkoord op het plan.

- **Altijd voor alle vier de agents.** Ook als de deelnemer nu maar één agent
  gebruikt. Zo is het project ook beschermd als iemand later, of per ongeluk,
  met een andere agent werkt.
- **Eén script en één lijst.** Alle agents gebruiken hetzelfde script. De lijst
  met verboden paden staat op één plek: de Read- en Edit-regels in
  `.claude/settings.json`.

| Sjabloon | Doel in het project | Wat het doet |
| --- | --- | --- |
| `bescherm-gevoelige-data.py` | `.agents/hooks/bescherm-gevoelige-data.py` | Zie hieronder. |
| `claude-settings.json` | `.claude/settings.json`, samengevoegd met bestaande instellingen | Dit is de lijst met verboden paden: de leesblokkades uit de basis, plus `output/`, `logs/runtime/` en `tmp/`. Er komen ook wijzigblokkades bij voor de instellingen en de hookconfiguraties van alle agents. Het bestand roept de beschermhook aan voor Claude Code, met `onFailure: block`. De projectmap-hook uit de basis blijft staan. |
| `codex-hooks.json` | `.codex/hooks.json` | Roept de hook aan voor Codex, vooraf en achteraf. |
| `copilot-hooks.json` | `.github/hooks/teamnl-bescherming.json` | Roept de hook aan voor Copilot (CLI, cloudagent en VS Code), vooraf en achteraf. |
| `vibe-hooks.toml` | `.vibe/hooks.toml` | Roept de hook aan voor Vibe, vooraf en achteraf, met `strict = true`. |
| `gitleaks.toml` | `.gitleaks.toml` | Gitleaks-regels voor persoonsnummers, naast de standaardregels voor secrets. |

**Wat het script `bescherm-gevoelige-data.py` doet:**

- **Vooraf** weigert het acties op de verboden paden. Dat geldt ook via
  shellcommando's, zoekopdrachten, patches, jokertekens en recursief zoeken
  vanuit een bovenliggende map. Het weigert ook commando's met de
  [echte-data-sleutel](veilig-verwerken.md#1-paden-via-configuratie). Staat die
  sleutel in de omgeving van de agent, dan weigert het elk shellcommando.
- **Achteraf** maskeert het paspoort-, ID- en BSN-nummers in de uitvoer, voordat
  het model die ziet.
- **Bij een interne fout** weigert het, in het formaat van de agent.
- **Zelftest.** Het script heeft een zelftest.

Zo richt je het in:

1. **Externe mappen toevoegen.** Voeg de mappen uit `DATA_DIR`, `OUTPUT_DIR` en
   `LOG_DIR` als leesblokkade toe aan `.claude/settings.json`, met een absoluut
   pad. Op Windows schrijf je `C:\Data\project` als `Read(//c/Data/project/**)`.
   Op macOS of Linux schrijf je `Read(//Users/naam/data/project/**)`. De hooks
   van alle agents lezen deze regels.
2. **Python-commando controleren.** Voor Claude Code en Vibe gebruikt het sjabloon
   `python`. Werkt op macOS of Linux alleen `python3`? Pas het commando dan aan.
   De sjablonen voor Codex en Copilot hebben al een commando per systeem. Het
   script vraagt Python 3.8 of nieuwer.
3. **Zelftest draaien:** `python .agents/hooks/bescherm-gevoelige-data.py --zelftest`.
4. **Activeren per agent.** Dit kan alleen de gebruiker:

   | Agent | Wat de gebruiker doet |
   | --- | --- |
   | Claude Code | Herstart de sessie. `onFailure` vraagt v2.1.295 of nieuwer. |
   | Codex | Vertrouw het project en keur de hook goed: `/hooks` in de CLI, of Settings > Hooks in de app. Na elke wijziging van `.codex/hooks.json` moet je opnieuw goedkeuren, want tot dan staat de hook uit. |
   | GitHub Copilot | **CLI:** vertrouw de map en herstart, want de hooks laden bij de start. **VS Code:** kies de Copilot-harness bij Session Target; hooks zijn daar nog in preview. **Cloudagent:** de hooks werken pas als het bestand op de standaardbranch staat. |
   | Mistral Vibe | Vertrouw de map en start Vibe vanuit de root van de repo. Gebruik versie 3.0.2 of nieuwer. |

5. **Toegangstests.** Voer de toegangstests 1 tot en met 5 uit voor elke agent
   die in het project wordt gebruikt. Een agent waarvoor ze niet slagen, gebruik
   je niet in dit project.

**Wat de hooks niet tegenhouden:**

- **Bij elke agent:**
  - een script dat zelf bestanden opent, of een pad dat via een variabele wordt
    opgebouwd;
  - persoonsgegevens zonder vast formaat in de uitvoer, zoals namen, HRV-waarden
    of geboortedata.

  Daarom staat de echte data buiten de repo, draait de agent geen code op echte
  data, gebruikt de code de echte-data-sleutel en bewijst de lektest dat de code
  niets laat uitlekken. Zie [veilig-verwerken.md](veilig-verwerken.md).
- **Codex.** Ontbreekt Python of duurt de hook langer dan de time-out? Dan gaat
  de actie door. Zonder goedkeuring via `/hooks` staat de hook uit, en dan kan
  Codex de hele schijf lezen.
- **Copilot.**
  - Een time-out laat de actie door.
  - Copilot leest ook de hooks in `.claude/settings.json`. Controleer dus dat
    gewone acties daar niet onterecht worden geweigerd.
- **Vibe.** Het is niet gedocumenteerd of hooks ook draaien bij automatisch
  goedkeuren. Gebruik dat bij dit project niet.
- **Bewust uitschakelen.** De hooks beschermen tegen ongelukken, niet tegen
  iemand die ze bewust uitzet, bijvoorbeeld met een vlag als
  `--dangerously-bypass-hook-trust`.

**Gevolgen voor het werk:**

- **Aanpassingen aan de instellingen, de hook of de hookconfiguraties.** Die
  doet de gebruiker zelf, buiten de agent om. Dat geldt ook bij een update van
  de basis. De agent laat dan het verschil zien.
- **Resultaten controleren.** De agent kan `output/` niet lezen. Hij controleert
  resultaten via tests met fictieve data.

## Toegangsgrenzen testen

Test met fictieve bestanden, nooit met echte gevoelige data. Gebruik
bijvoorbeeld `data/private/proef-niet-lezen.txt` en een `.env`, elk met de tekst
`PROEF-GEHEIM-12345`. Bij risiconiveau hoog maak je ook een proefbestand in
`logs/runtime/` en in de externe datamap. De gebruiker maakt de proefbestanden
zelf. De agent kan dat niet, want de leesblokkades verhinderen ook het schrijven
op die plekken.

Het [risiconiveau](data-afspraken.md#risiconiveau) bepaalt welke controles
verplicht zijn:

| Niveau | Controles |
| --- | --- |
| Laag | 1 tot en met 3 |
| Gevoelig | 1 tot en met 4 |
| Hoog | 1 tot en met 5 |

Voer ze uit per agent die de deelnemer gebruikt:

1. **Direct lezen.** Vraag de agent het proefbestand te openen. De verwachting:
   geweigerd.
2. **Via een opdracht.** Vraag de agent `cat`, `type` of `Get-Content` uit te
   voeren op het proefbestand. Probeer ook `grep -r PROEF .` vanuit de root.
   Bij hoog probeer je daarnaast een commando met `TEAMNL_ECHTE_DATA=1`. Noteer
   of dit wordt geblokkeerd.
3. **Uitvoer terug.** Laat een script het proefbestand verwerken. Controleer of
   alleen de afgesproken samenvatting terugkomt, en niet `PROEF-GEHEIM-12345`.
4. **Lekpaden.** Draai de lektest uit
   [veilig-verwerken.md](veilig-verwerken.md#5-lektest), of laat het programma
   nepdata met herkenbare nepwaarden verwerken. Zoek de nepwaarden terug in deze
   plekken; ze mogen er nergens in staan:
   - de schermuitvoer en de foutmeldingen;
   - `logs/`;
   - `output/`;
   - `tmp/`.

   Controleer bij hoog ook dat een getoond paspoortnummer in de uitvoer als
   `[GEMASKEERD]` bij de agent aankomt.
5. **Hook ontbreekt of faalt.** Hernoem het hookscript tijdelijk en herhaal
   controle 1 en 2. Je verwacht bij elke agent: geweigerd. Controleer ook dat
   een gewone actie, zoals het lezen van `README.md`, met een werkende hook wel
   lukt. Zet het script daarna terug.

Verwijder de proefbestanden daarna. Leg per agent in
`docs/agent-startcontrole.md` vast:

- de versie en de datum;
- wat is geblokkeerd;
- wat niet is geblokkeerd;
- wat onbekend blijft.

Een niet-geblokkeerde route is een beperking, en geen reden om echte data toch
toegankelijk te maken.

## Bronnen

- [Codex-skills](https://learn.chatgpt.com/docs/build-skills) ·
  [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) ·
  [Codex-permissies](https://learn.chatgpt.com/docs/permissions) ·
  [Codex-hooks](https://learn.chatgpt.com/docs/hooks.md)
- [Claude Code-skills](https://code.claude.com/docs/en/skills) ·
  [permissies](https://code.claude.com/docs/en/permissions) ·
  [hooks](https://code.claude.com/docs/en/hooks) ·
  [sandboxing](https://code.claude.com/docs/en/sandboxing) ·
  [geheugen en AGENTS.md](https://code.claude.com/docs/en/memory)
- [Copilot agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) ·
  [instructiebestanden](https://docs.github.com/en/copilot/reference/custom-instructions-support) ·
  [hooks](https://docs.github.com/en/copilot/reference/hooks-reference) ·
  [hooks in VS Code](https://code.visualstudio.com/docs/agent-customization/hooks) ·
  [content exclusion](https://docs.github.com/en/copilot/concepts/context/content-exclusion)
- [Mistral Vibe-skills](https://docs.mistral.ai/vibe/code/cli/skills) ·
  [AGENTS.md](https://docs.mistral.ai/vibe/code/cli/agents) ·
  [configuratie](https://docs.mistral.ai/vibe/code/cli/configuration-reference) ·
  [hooks](https://docs.mistral.ai/vibe/code/cli/hooks)
