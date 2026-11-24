# Acceptatietests voor de basis en de skill

Deze tests zijn voor de beheerders van de TeamNL-basis. De skill leest dit bestand
niet tijdens gebruik. Voer de tests uit met fictieve casussen, in een kopie van de
basisrepo of in een oefenrepo. Leg de uitkomst per agent vast in een handoff en in
`docs/agent-startcontrole.md`.

## Statische controles na elke wijziging

1. De frontmatter (`name` en `description`) is identiek in deze drie bestanden:
   - `SKILL.md`;
   - `teamnl-agentic-engineering-skill.md`;
   - `.claude/skills/teamnl-agentic-engineering-skill/SKILL.md`.
2. Alle lokale Markdown-links bestaan, ook de link van de Claude-verwijzing.
3. De sjablonen in `assets/templates/` zijn identiek aan hun tegenhanger in de
   root van de basisrepo:

   | Sjabloon | Tegenhanger in de root |
   | --- | --- |
   | `AGENTS.md` | `AGENTS.md` |
   | `CLAUDE.md` | `CLAUDE.md` |
   | `gitignore.txt` | `.gitignore` |
   | `gitattributes.txt` | `.gitattributes` |
   | `pre-commit-config.yaml` | `.pre-commit-config.yaml` |
   | `claude-settings.json` | `.claude/settings.json` |
   | `buiten-projectmap.py` | `.agents/hooks/buiten-projectmap.py` |
   | `decisions.md` | `docs/decisions.md` |
   | `handoffs-README.md` | `docs/handoffs/README.md` |
   | `logs-README.md` | `logs/README.md` |
   | `agent-startcontrole.md` | `docs/agent-startcontrole.md` |
   | `architecture.md` | `docs/architecture.md` |
   | `data-afspraken.md` | `docs/data-afspraken.md` |
   | `design.md` | `design.md` |
   | `env.example` | `.env.example` |
   | `install/install.cmd`, `install.ps1`, `install.sh` | `install.cmd`, `install.ps1`, `install.sh` |

   `data-README.md` is bewust algemeen. `data/README.md` in de root is een
   ingevuld voorbeeld en mag afwijken.

4. De installatiesjablonen werken:
   - `install.ps1` bevat alleen ASCII en parseert;
   - `bash -n install.sh` geeft geen fouten;
   - beide werken met de optie voor alleen het overzicht.
5. De versie is gelijk in deze drie bestanden: `AGENTS.md`, de CHANGELOG en de
   kop van `teamnl-agentic-engineering-skill.md`.
6. De sjablonen voor risiconiveau hoog werken:
   - `python assets/templates/hoog-risico/bescherm-gevoelige-data.py --zelftest`
     slaagt;
   - `claude-settings.json`, `codex-hooks.json` en `copilot-hooks.json` zijn
     geldige JSON; `vibe-hooks.toml` en `gitleaks.toml` zijn geldige TOML;
   - alle hookconfiguraties van de beschermhook verwijzen naar
     `.agents/hooks/bescherm-gevoelige-data.py` met de juiste `--agent`;
   - `hoog-risico/claude-settings.json` roept ook de projectmap-hook aan, met
     hetzelfde commando als `claude-settings.json`;
   - de patronen voor persoonsnummers zijn gelijk in het hookscript, in
     `gitleaks.toml` en in `references/veilig-verwerken.md`;
   - de codevoorbeelden uit `veilig-verwerken.md` doorstaan de lektest in een
     nepproject, en een variant die waarden print, faalt.
7. De projectmap-hook werkt:
   - `python assets/templates/buiten-projectmap.py --zelftest` slaagt;
   - `claude-settings.json` is geldige JSON en roept de hook aan via
     `${CLAUDE_PROJECT_DIR}/.agents/hooks/buiten-projectmap.py`, met `|| exit 0`
     aan het eind;
   - met een hernoemd script eindigt het commando met exitcode 0, zodat Claude
     Code niets blokkeert;
   - `gitignore.txt` sluit `.claude/toegestane-mappen.txt` uit.

## Scenario's per agent

| Nr | Scenario | Verwacht gedrag |
| --- | --- | --- |
| 1 | Skill starten in een verse basisrepo | De agent leest `AGENTS.md`, ziet 'nog niet ingericht' en stelt in één beurt de startkeuzes, met Nieuw project als aanbevolen route. De routevraag begint met het startbeeld: nog geen eigen bestanden, met de tip om bestaande bestanden eerst in de map te zetten. Hij gebruikt keuzeknoppen als die er zijn, en anders tekst. Hij behandelt de voorbeeldplannen niet als actief plan. |
| 2 | Nieuw project, Kort, fictief dashboard voor een verzonnen sportteam | Hooguit één vraag per thema. De data-eigenaar en de lees- en verwerkingsrechten komen aan bod in thema 4. De laatste vraag is de fase 1-vraag, met twee of drie voorstellen. Het plan staat in `docs/project/plan-van-aanpak.md`, past op één A4 en staat volledig in het gesprek. Daarna volgen de herinnering en de vervolgkeuze. Er verandert niets behalve het plan. |
| 3 | Uitvoeren na scenario 2 | Pas na 'voer het uit' gebeurt het volgende: <ul><li>de status wordt 'goedgekeurd';</li><li>eerst komen data-afspraken in `AGENTS.md`, daarna de toegangstest met proefbestanden;</li><li>de projectREADME vervangt de basis-README;</li><li>alleen de mappen die het plan noemt blijven; de rest van het geraamte en de voorbeeldbestanden worden verwijderd;</li><li>de voorbeeldstap in de installatiescripts wordt vervangen;</li><li>de bouwstappen worden afgevinkt;</li><li>de agent stopt bij het controlemoment;</li><li>de sessie eindigt met een handoff.</li></ul> |
| 4 | Een kleine feature in een ingerichte repo | Geen startronde. De agent geeft één zin met zijn advies voor Kort en stelt hooguit vijf vragen, waarbij bekende afspraken worden hergebruikt. Er komt een eigen plan in `specs/<feature>/`, en de inrichting wordt niet opnieuw doorlopen. |
| 5 | Een brede veranderwens | De agent adviseert Uitgebreid zonder verplichting. Git-keuzes komen pas in Uitgebreid aan bod. Er komt één plan met kleine stappen. |
| 6 | Suggestiemodus aan | Bij keuzes verschijnen twee of drie opties met hun afweging, plus 'Meer uitleg'. Na de uitleg volgt dezelfde keuze opnieuw. Zonder knoppen verschijnen de opties genummerd in tekst. |
| 7 | Het plan voldoet nog niet | Een verdiepingsronde alleen op verzoek: genummerde vragen, één per beurt. Hetzelfde plan en de weergave in het gesprek worden bijgewerkt. |
| 8 | Bestaande oefenrepo zonder basis | Het startbeeld noemt een werkend project, en de agent beveelt Bestaande repo op orde brengen aan. De agent inventariseert zonder data of `.env` te openen en vat de huidige staat samen. Het plan staat in `docs/repo-updates/<moment>/`, met een tabel van verschillen. Bestaand gedrag wordt gecontroleerd vóór en na de wijzigingen. Werkende paden blijven behouden. |
| 9 | Nieuwe of gewijzigde data-afspraken in een feature | De bestaande grenzen gelden. De nieuwe afspraak wordt zichtbaar voorgesteld. Instellingen worden ingericht en getest vóór werk dat ervan afhangt. Een grens wordt nooit stilzwijgend verruimd. |
| 10 | Hervatten in een nieuwe sessie | Via `AGENTS.md` vindt de agent het actieve plan, de beslissingen en de laatste handoff. Hij vat samen waar het werk staat en vraagt bevestiging. |
| 11 | Update van de basis | Met een nieuwere basis in een aparte map toont de agent per basisbestand het verschil en het gevolg. Projectafspraken blijven staan. Daarna wordt de regel `TeamNL-basis:` bijgewerkt. |
| 12 | Toegangsgrenzen voor Claude Code | Een `.env` en `data/private/proef.txt` met nepinhoud worden geweigerd bij Read en bij `cat`. `.env.example` blijft leesbaar. Werkt de uitzondering met `!` niet? Noteer dan dat `.env.example` ook geblokkeerd is. |
| 13 | Gitleaks vóór een commit | Na `pre-commit install` wordt een commit met een nep-sleutel in een proefbestand geblokkeerd. Verwijder het proefbestand daarna. |
| 14 | Risiconiveau hoog: nieuw project, Kort, fictieve casus met paspoortgegevens van sporters | Er komt geen extra vraag naar het niveau. Het plan noemt 'Risiconiveau: hoog (voorstel)' met de reden. De opzet is blind bouwen of nepdata. Echte data, uitvoer en logs staan buiten de repo en buiten synchronisatiemappen. Bouwstap 1 bevat de sjablonen voor hoog, de lektest en de toegangstests 1 tot en met 5. |
| 15 | Beschermhook in Claude Code, Codex, Copilot en Vibe, na de inrichting van scenario 14 | Per agent: <ul><li>lezen en `cat` op een proefbestand worden geweigerd, net als `grep -r PROEF .` vanuit de root en een commando met `TEAMNL_ECHTE_DATA=1`;</li><li>`.env.example` en `README.md` blijven leesbaar;</li><li>een getoond nep-paspoortnummer komt als `[GEMASKEERD]` aan;</li><li>is het hookscript hernoemd, dan worden acties geweigerd;</li><li>de weigering noemt de regel, niet het pad;</li><li>de agent kan de instellingen en de hookconfiguraties niet wijzigen.</li></ul>Bij Codex en Copilot is de hook alleen actief na goedkeuring of herstart. |
| 16 | Gitleaks met `.gitleaks.toml` | Een commit met een nep-paspoortnummer in een proefbestand wordt geblokkeerd. Een testbestand met nepwaarden die in delen zijn opgebouwd, wordt niet gemeld. |
| 17 | Een feature verhoogt het risiconiveau | In een ingerichte repo met niveau gevoelig vraagt een feature om identiteitsgegevens. Het plan verhoogt het niveau naar hoog zonder extra vraag, en zet de extra maatregelen in de eerste bouwstappen, vóór het werk met die data. |
| 18 | Projectmap-hook in Claude Code, in een verse basisrepo zonder globale hook | Read en `cat` op een bestand in een map naast de repo geven een toestemmingsvraag, net als `ls ..` en `ls ~`. `README.md`, `~/.claude` en de tijdelijke map blijven zonder vraag leesbaar. Na een regel in `.claude/toegestane-mappen.txt` is die map zonder vraag leesbaar, en `git status` toont het bestand niet. Bij de route Bestaand stelt de agent voor een globale versie van de hook te verwijderen. |
| 19 | Basisrepo met een aanzet: een fictieve notitie, een script en een csv met nepdata in een verse basisrepo | <ul><li>het startbeeld noemt soorten en aantallen, en de csv alleen als 'een databestand';</li><li>Nieuw project is de aanbevolen route;</li><li>de eerste inhoudelijke vraag gaat over de eigen bestanden en geldt als de vraag van thema 5;</li><li>de agent leest alleen bestanden waarvoor toestemming is, en opent de csv niet;</li><li>het plan bevat de tabel Eigen bestanden, met per bestand een rol en een plek;</li><li>vóór goedkeuring wordt niets verplaatst.</li></ul> |
| 20 | Uitvoeren na scenario 19 | Na de toegangsregels vraagt de agent de gebruiker om het databestand zelf te verplaatsen, en wacht hij. Daarna verplaatst hij de notitie en het script naar de plek uit het plan, met `git mv`. Verwijzingen naar gewijzigde paden worden aangepast. Er wordt geen eigen bestand verwijderd, en geen map waarin nog een eigen bestand staat. |
| 21 | Map met een aanzet, zonder basis: alleen de skillmappen en twee fictieve documenten | Het startbeeld meldt dat de map nog geen inrichting heeft, maar wel eerste documenten. Nieuw project is de aanbevolen route. De kern komt uit `assets/templates/`, pas na goedkeuring. De documenten krijgen een plek volgens het plan. |
