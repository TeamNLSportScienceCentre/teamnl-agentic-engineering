# Versiegeschiedenis: TeamNL-standaardrepo en skill

De skill hoort bij de standaardrepo. Een project noteert de gebruikte versie in
`AGENTS.md`, in de regel `TeamNL-basis:`.

## Standaardrepo 1.3.0 · skill 2.3.0 · 24 november 2026

Beginnen met eigen bestanden. Een deelnemer kan een nieuw project starten in een
map waarin al een aanzet staat, zoals notities, documentatie of een eerste
script. Die bestanden kunnen startmateriaal zijn, niet alleen eerder werk.

**Skill**

- **Startsituatie in twee stappen.** Eerst bepaalt de skill welke van de vier
  situaties het is. Daarna kijkt hij of er eigen bestanden staan: geen, een
  aanzet of een werkend project. Hij kijkt daarvoor alleen naar namen, soorten
  bestanden en mappen, en opent geen inhoud. Een aanzet leidt naar Nieuw
  project, een werkend project naar Bestaande repo op orde brengen.
- **Startbeeld.** De routevraag begint met één of twee zinnen over wat de skill
  zag, met soorten en aantallen. Een databestand noemt hij alleen als soort. Zonder
  eigen bestanden volgt de tip om bestaande bestanden eerst in de map te zetten.
- **Vraag over eigen bestanden.** In de route Nieuw project is dat de eerste
  inhoudelijke vraag: waarvoor zijn ze, mag de agent ze lezen en mag hij een plek
  voorstellen? De vraag geldt als de vraag van thema 5, dus er komt geen vraag
  bij. Thema 3 vraagt daarna alleen nog naar materiaal buiten de map.
- **Drie rollen.** Elk eigen bestand krijgt in het plan een rol: startmateriaal,
  referentie of data. De gebruiker kiest. Bij twijfel stelt de skill referentie
  voor. Code of eerder werk buiten de map blijft referentie.
- **Plansjablonen.** Het korte en het uitgebreide plan voor een nieuw project
  hebben een tabel Eigen bestanden, met per bestand de rol en de plek.
- **Inrichting.** Een nieuwe stap Eigen bestanden ordenen, na de data-afspraken:
  - de gebruiker verplaatst databestanden zelf, omdat de toegangsregels de plek
    ook voor de agent blokkeren;
  - de agent verplaatst de rest met `git mv`, of legt zonder Git in het plan vast
    wat waarheen ging;
  - een secret in startcode wordt niet getoond, maar vervangen door een
    verwijzing naar `.env`;
  - er wordt geen eigen bestand verwijderd, en geen map waarin nog een eigen
    bestand staat.

**Standaardrepo**

- **README.** Een nieuwe stap bij Snel starten: zet je eerste bestanden in de
  map, maar nog geen echte data. De sectie over een bestaande repository geldt
  nu ook voor een bestaande map, met de route die de skill aanbeveelt.
- **Acceptatietests.** Scenario 1 en 8 controleren het startbeeld. Nieuwe
  scenario's 19 tot en met 21 gaan over een basisrepo en een map met een aanzet.

**Nog niet getest**

- De scenario's 1, 8 en 19 tot en met 21 in een echte sessie.

## Standaardrepo 1.2.0 · skill 2.2.0 · 19 november 2026

Hooks per project in plaats van per gebruiker. De projectmap-hook zat eerder
in de instellingen van één gebruiker (`~/.claude/settings.json`) en gold zo voor
al diens projecten. Nu zit hij in de basis en richt de skill hem per project in.

**Standaardrepo**

- **Nieuwe projectmap-hook `.agents/hooks/buiten-projectmap.py`**, met sjabloon
  `assets/templates/buiten-projectmap.py`. Claude Code vraagt om toestemming
  voordat het buiten de projectmap leest of zoekt.
  - Zonder vragen toegestaan: de projectmap, `~/.claude`, de tijdelijke map,
    `additionalDirectories` en de mappen in `.claude/toegestane-mappen.txt`.
  - Herkent paden voor Windows, Git Bash, macOS en Linux, de thuismap en `..`.
  - Heeft een zelftest: `--zelftest`.
  - Bij een fout gaat de actie door. De hook is een vangnet, geen
    beveiligingsgrens. Het commando eindigt op `|| exit 0`: zonder die
    toevoeging zou een ontbrekend script (Python-exitcode 2) elke lees- en
    zoekactie blokkeren.
- **`.claude/settings.json`** en het sjabloon roepen de hook aan bij
  `PreToolUse`. Het sjabloon voor risiconiveau hoog doet dat ook, naast de
  beschermhook.
- **`.claude/toegestane-mappen.txt`** bevat de vaste uitzonderingen per project.
  Het staat in `.gitignore`, omdat paden per computer verschillen.
- **`docs/agent-startcontrole.md`** heeft een tabel voor de projectmap-hook.
- **`AGENTS.md`** noemt de hook en de regel voor mappen buiten de projectmap.

**Skill**

- `agent-inrichting.md` heeft een nieuwe paragraaf 'Projectmap-hook (Claude
  Code)': wat de hook doet, hoe je hem inricht, hoe je een uitzondering
  vastlegt en wat hij niet tegenhoudt.
- De routes Nieuw project en Bestaand controleren de hook bij de stap
  Data-afspraken of Toegangsregels. Staat er nog een globale versie van de hook
  bij de gebruiker? Dan stelt de skill voor om die te verwijderen.
- Een nieuwe vaste grens: hooks horen in het project, niet in de instellingen
  van de gebruiker. Een map buiten de repo komt pas na akkoord in
  `.claude/toegestane-mappen.txt`, en de keuze komt in `docs/decisions.md`.

**Getest en niet getest**

- **Wel getest, op Windows 11 met Git Bash:**
  - de zelftest van het hookscript: 30 gevallen, ook via stdin;
  - het commando uit `.claude/settings.json`: een vraag bij een pad buiten
    het project, stilte binnen het project, en exitcode 0 bij een ontbrekend
    script;
  - in een lopende sessie van Claude Code: de hook uit de projectinstellingen
    draait zonder herstart, en `CLAUDE_PROJECT_DIR` wordt ingevuld.
- **Nog niet getest:**
  - de zelftest op macOS en Linux;
  - Claude Code op Windows zonder Git Bash, dat dan PowerShell gebruikt;
  - de hook in Copilot, dat de hooks in `.claude/settings.json` ook leest.

## Standaardrepo 1.1.0 · skill 2.1.0 · 19 november 2026

Extra bescherming voor gevoelige data, voor alle ondersteunde agents.

**Skill**

- **Risiconiveaus.** Er zijn drie niveaus: laag, gevoelig en hoog. De skill leidt
  het niveau af uit het antwoord op de datavraag, zonder extra vraag, en zet het
  met de reden in het plan. Elk niveau heeft verplichte maatregelen. Bij hoog
  zijn dat:
  - alleen blind bouwen of bouwen op nepdata;
  - echte data, uitvoer en logs buiten de repo en buiten synchronisatiemappen
    zoals OneDrive;
  - de beschermhook voor alle vier de agents;
  - de echte-data-sleutel;
  - maatregelen in de code;
  - een lektest;
  - Gitleaks-regels voor persoonsnummers.
- **Nieuwe referentie `veilig-verwerken.md`.** Die beschrijft:
  - **de echte-data-sleutel.** De code raakt echte data alleen als de gebruiker
    `TEAMNL_ECHTE_DATA=1` zelf in een eigen terminal zet. Zonder sleutel valt de
    code terug op fictieve data. Een agent die het programma per ongeluk start,
    raakt zo geen echte data;
  - paden via configuratie, met een controle bij het starten;
  - alleen samenvattingen tonen;
  - foutmeldingen zonder waarden;
  - een logfilter;
  - een lektest met nepwaarden.
- **Toegangstests.** Er is een vijfde test bijgekomen: lekpaden via uitvoer,
  logs, uitvoerbestanden en tijdelijke bestanden. Het risiconiveau bepaalt welke
  tests verplicht zijn. Een agent waarvoor de tests bij hoog niet slagen,
  gebruik je niet in het project. De gebruiker maakt de proefbestanden, omdat de
  leesblokkades de agent ook het schrijven verhinderen.
- **Plansjablonen en routes.** Ze noemen het risiconiveau, en een feature kan het
  niveau verhogen.
- **Inrichting per agent.** `agent-inrichting.md` beschrijft per agent:
  - de hooks;
  - het gedrag bij een falende hook;
  - de stappen die de gebruiker moet doen om de hook te activeren;
  - de restrisico's.

  De gegevens zijn nagelopen in de documentatie van 18 november 2026.

**Standaardrepo**

- **Nieuwe sjablonen in `assets/templates/hoog-risico/`.** Ze komen alleen in een
  project met risiconiveau hoog, niet in de basis, en dan altijd voor alle vier de
  agents:
  - `bescherm-gevoelige-data.py`: één hookscript voor Claude Code, Codex, GitHub
    Copilot en Mistral Vibe, met een zelftest;
  - `claude-settings.json`: de enige lijst met verboden paden. Die bevat
    wijzigblokkades op de instellingen en hookconfiguraties van alle agents;
  - `codex-hooks.json`, `copilot-hooks.json` en `vibe-hooks.toml`: de aanroep van
    de hook per agent;
  - `gitleaks.toml`: regels voor persoonsnummers.
- **Wat het hookscript doet.**
  - *Vooraf:* het weigert acties op de verboden paden. Dat geldt ook via
    shellcommando's, zoekopdrachten, patches, jokertekens en recursief zoeken.
    Het weigert ook commando's met de echte-data-sleutel, en alle
    shellcommando's als die sleutel in de omgeving van de agent staat.
  - *Achteraf:* het maskeert paspoort-, ID- en BSN-nummers in de uitvoer.
  - *Bij een fout:* het weigert de actie, in het formaat van de agent.
- **Kleine aanpassingen in bestaande bestanden:**
  - `.env.example` noemt ook `OUTPUT_DIR` en `LOG_DIR`;
  - `logs/README.md` beschrijft de logs bij hoog;
  - `docs/data-afspraken.md` heeft een kolom voor het risiconiveau;
  - `docs/agent-startcontrole.md` heeft een kolom voor de lektest en een regel
    per agent.
- **Opgeschoond.** De ontwikkelverslagen van de basis staan niet meer in
  `docs/handoffs/`. Die map bevat in de basis alleen nog de README. De
  geschiedenis van de basis staat in deze CHANGELOG.

**Getest en niet getest**

- **Wel getest:**
  - de zelftest van het hookscript: 69 gevallen, met de invoer- en
    antwoordformaten van alle vier de agents;
  - de aanroep via stdin;
  - de codevoorbeelden uit `veilig-verwerken.md`, inclusief de
    echte-data-sleutel, in een nepproject.
- **Nog niet getest:**
  - de hooks in een echte sessie van Claude Code, Codex, Copilot en Vibe;
  - `gitleaks.toml` met Gitleaks zelf.

## Standaardrepo 1.0.0 · skill 2.0.0 · 17 november 2026

Eerste versie van de standaardrepo. De intake-skill is uitgebreid tot een skill
met drie routes en heet nu `teamnl-agentic-engineering-skill`. Gebaseerd op de
ontwerpdocumenten 'Standaardrepository voor TeamNL projecten' en 'Uitbreiding
van de TeamNL intake skill' van 16 november 2026.

**Standaardrepo**

- Compacte kern met:
  - `README.md`, `AGENTS.md` en `CLAUDE.md`;
  - `.gitignore`, `.gitattributes` en de Gitleaks-controle vóór een commit;
  - standaard leesblokkades voor Claude Code;
  - `docs/decisions.md`, `docs/handoffs/`, `docs/agent-startcontrole.md` en `logs/`.
- Vaste locaties voor plannen: `docs/project/`, `specs/<feature>/` en
  `docs/repo-updates/<moment>/`.
- Het volledige geraamte is zichtbaar: alle standaardmappen, elk met een korte
  README, en `.gitkeep` waar de inhoud buiten Git blijft. Er zijn
  voorbeeldbestanden voor één fictieve casus:
  - drie voorbeeldplannen;
  - voorbeelddata;
  - een testbestand;
  - een voorbeeldafbeelding.

  Ook staan `design.md`, `.env.example` en de installatiescripts al in de root.
  Bij de inrichting houdt een project alleen wat het nodig heeft. De skill
  verwijdert de rest en de voorbeelden, na akkoord op het plan.
- Sjablonen in `assets/templates/` zodat de skill ook buiten de basisrepo werkt:
  - de bestanden van de kern;
  - een projectREADME en de README's voor data en logs;
  - de handoff;
  - `design.md` met de TeamNL-stijl;
  - installatiescripts voor Windows en macOS/Linux.
- De naam `docs/decisions.md` is gekozen in kleine letters. Het naslagwerk
  noemt elders `DECISIONS.md`.

**Skill (was teamnl-agentic-engineering-intake-skill 1.x)**

- Drie routes: nieuw project, bestaande repo op orde brengen (inclusief een
  update van de basis) en nieuwe feature.
- De korte feature-intake telt hooguit vijf vragen, inclusief keuze- en
  verduidelijkingsvragen. De route Nieuw project behoudt de acht thema's en de
  limieten uit versie 1. De route Bestaand gebruikt zes thema's met dezelfde
  limieten per thema.
- Een optionele suggestiemodus: twee of drie opties met uitleg, en de optie
  'Meer uitleg'.
- Git-keuzes komen alleen in de uitgebreide intake aan bod. De uitzondering is
  nieuwe gevoelige onderdelen.
- Het plan wordt opgeslagen op de standaardlocatie, zonder een ander plan te
  overschrijven, en staat altijd leesbaar in het gesprek.
- Na expliciete goedkeuring voert de skill het plan uit:
  - in kleine bouwstappen met controlemomenten;
  - met automatische tests;
  - met bijgewerkte `AGENTS.md`, beslissingen en handoffs.
- De verdiepingsronde start alleen op verzoek, met hooguit tien vragen per ronde.
- De ingangen per agent zijn gecontroleerd tegen de documentatie van
  17 november 2026. Copilot gebruikt `.agents/skills/`, dus een aparte ingang
  is niet nodig. In de praktijk is nog niets getest.

**Voorlopig, nog af te stemmen**

- De vraaglimieten voor de routes Nieuw en Bestaand, voor Uitgebreid bij een
  feature en voor de verdiepingsronde.
- De definitieve bestandslocaties.
- De uitvoering van keuzeknoppen per plugin.
- De distributie van de basis en het overnemen van updates.
- Welke TeamNL-logo's mee mogen.

## Intake-skill 1.x · oktober tot november 2026

De versie in de cursusrepository `teamnl-agentic-engineering`, commit 4c20fc5.
Die versie bood een korte of uitgebreide intake met acht thema's en leverde
alleen een plan, zonder wijzigingen aan de repository.
