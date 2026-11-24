# teamnl-agentic-engineering

Een mini-app voor de **TeamNL Agentic Engineering-dagen**. Vul een nepaccountnaam
en nepwachtwoord in, sla ze op en ontdek waarom `.env` buiten Git hoort.

**Gebruik nooit een echt wachtwoord, API-key, e-mailadres of andere echte gegevens.**
Dit is speelgoed. Een `.env` is gewone leesbare tekst, geen beveiligde kluis.

## Starten zonder installatie

1. Open de map van deze repository.
2. Dubbelklik op **index.html**. De app opent in je browser op Windows of macOS.
3. Vul de twee velden in, bijvoorbeeld `nep-cursist` en `voorbeeld-123`.
4. Klik op **.env opslaan**.
5. Bewaar het bestand als **.env** in dezelfde map als `index.html`.

De app heeft geen Python, Java, Node.js, account of internetverbinding nodig.
Alleen een bestaande browser. Chrome en Edge bieden waar ondersteund een
opslaanvenster; Firefox en Safari gebruiken een download. Verplaats een download
zelf naar de repository. Controleer de naam: `.env`, zonder `.txt` of `(1)`.
Opnieuw opslaan op dezelfde plek vervangt de eerdere oefengegevens; kies nooit
een `.env` van een ander project.

**Bestand niet zichtbaar?** Op macOS toont `Cmd + Shift + .` verborgen bestanden
in Finder. In het opslaanvenster kun je `Cmd + Shift + G` gebruiken om naar de
repositorymap te gaan. Zet op Windows in Verkenner bij **Weergeven → Weergeven**
de opties **Verborgen items** en **Bestandsnaamextensies** aan.

## Welke bestanden leer je kennen?

| Bestand | Betekenis |
| --- | --- |
| `README.md` | Uitleg voor mensen: wat doet dit project en hoe start je het? |
| `AGENTS.md` | Opdracht en werkafspraken voor een coding agent. |
| `.gitignore` | Patronen van lokale bestanden die Git niet moet toevoegen. |
| `.env` | Jouw lokale nepcredentials; wordt pas bij opslaan gemaakt. |
| `.env.example` | Openbaar voorbeeld met verzonnen waarden; mag wel in Git. |
| `index.html` | Het venster van de app. |
| `src/` | De vormgeving en JavaScriptcode. |

De app schrijft de twee ingevulde waarden als `DEMO_USERNAME` en `DEMO_PASSWORD`.
Gebruik alleen verzonnen waarden die nergens als login dienen.
Andere apps kunnen hun instellingen uit een `.env` lezen; deze demo maakt alleen
het bestand en leest geen opgeslagen credentials terug.

## Oefening: clone → wijzig → commit → push

**Voor de Git-oefening moet Git al op de cursuscomputer staan.** Pushen vraagt
ook een GitHub-account en schrijfrechten op de gekozen repository. De app zelf
vereist dit niet. Laat de begeleider deze voorzieningen vooraf regelen als
cursisten niets mogen installeren. Met GitHub **Code → Download ZIP** kun je de
app ook openen zonder Git, maar daarmee oefen je geen clone, commit of push.

Open een terminal (PowerShell op Windows, Terminal op macOS):

```sh
git clone https://github.com/TeamNLSportScienceCentre/teamnl-agentic-engineering.git
cd teamnl-agentic-engineering
git switch -c oefening/jouw-unieke-naam
```

Vervang `jouw-unieke-naam` door een eigen herkenbare oefennaam. Zonder
schrijfrechten: maak eerst op GitHub een fork naar je eigen account en clone de
URL van die fork in plaats van de TeamNL-repository.

Open de app en bewaar `.env` in de repo. Controleer vervolgens:

```sh
git status --short
git check-ignore .env
```

`.env` mag niet als nieuw bestand in `git status` staan. Het tweede commando
moet `.env` tonen: de negeerregel werkt. Controleer ook zelf dat het bestand
bestaat; `git check-ignore` controleert een patroon, niet of je hebt opgeslagen.

Verander nu het label `Fictieve accountnaam` in `index.html` naar `Accountnaam (oefening)`, sla het bestand op en
ververs je browser. Leg die wijziging vast:

```sh
git diff
git add index.html
git diff --cached
git commit -m "Pas het veldlabel van mijn oefenapp aan"
git push -u origin HEAD
```

Een **commit** is een lokaal bewaard wijzigingspakket met een beschrijving.
Een **push** verstuurt je commits naar GitHub. Bekijk daar je eigen branch.
Als Git bij commit om een identiteit vraagt, stel voor deze repository
`git config user.name "Je naam"` en `git config user.email "Je GitHub-noreply-adres"`
in met je eigen waarden. Je noreply-adres vind je bij je GitHub-e-mailinstellingen.

**Let op:** `.gitignore` versleutelt niets en stopt geen bestanden die al door
Git gevolgd worden. Gebruik nooit `git add -f .env`. Voeg voor deze oefening
alleen je gewijzigde bronbestand toe. Deel je `.env` ook niet via screenshots.

## Een eigen project met de skill

De **teamnl-agentic-engineering-skill** begeleidt je van idee naar plan, en voert
dat plan uit nadat jij het hebt goedgekeurd. Hij vervangt de eerdere
`teamnl-agentic-engineering-intake-skill`. De skill staat in een aparte submap,
los van de appcode:

```text
.agents/skills/teamnl-agentic-engineering-skill/
|-- SKILL.md                              # Startbestand
|-- teamnl-agentic-engineering-skill.md   # Centrale instructies
|-- agents/openai.yaml
|-- references/            # Routes, plansjablonen, data, agents, installatie, stijl
|-- assets/templates/      # Sjablonen voor projectbestanden
|-- CHANGELOG.md           # Versies van de skill
`-- acceptatietests.md     # Tests voor beheerders
```

Codex, GitHub Copilot en Mistral Vibe vinden de skill in `.agents/skills/`.
Claude Code zoekt in `.claude/skills/`; daar staat alleen een korte verwijzing
naar dezelfde instructies. Pas de skill dus altijd aan in `.agents/skills/`.

### Starten in je eigen projectmap

Gebruik de skill in de map van je eigen project, niet in deze cursusrepo.

1. **Kopieer twee mappen** uit deze repository naar je projectmap:
   - `.agents/skills/teamnl-agentic-engineering-skill/`;
   - `.claude/skills/teamnl-agentic-engineering-skill/` (alleen nodig voor
     Claude Code).

   Mappen die met een punt beginnen, zijn soms verborgen. Zie 'Bestand niet
   zichtbaar?' bij [Starten zonder installatie](#starten-zonder-installatie).
2. **Zet je eerste bestanden erin, als je die al hebt.** Bijvoorbeeld notities,
   documentatie of een eerste script. Echte data zet je er nog niet in. Dat
   regel je met de skill bij de data-afspraken.
3. **Open je projectmap** in je editor of agent. Open niet je hele schijf of je
   gebruikersmap.
4. **Start de skill** in het gesprek met je agent:

   | Agent | Typ in het gesprek |
   | --- | --- |
   | Codex | `$teamnl-agentic-engineering-skill` |
   | Claude Code | `/teamnl-agentic-engineering-skill` |
   | GitHub Copilot | `/teamnl-agentic-engineering-skill` |
   | Mistral Vibe | `/teamnl-agentic-engineering-skill` (markeer de map eerst als vertrouwd) |

   Verschijnt de skill niet? Herstart dan je agentsessie.

### Wat de skill doet

De skill kijkt eerst wat er in je map staat, zonder data of `.env` te openen, en
vat dat in een paar zinnen samen. Daarna kies je in één beurt:

- **de route:** Nieuw project (een lege map of een paar eerste bestanden),
  Bestaande repo op orde brengen (een werkend project) of Nieuwe feature (een
  project dat al is ingericht);
- **de variant:** Kort voor een concrete, afgebakende wens, Uitgebreid voor een
  grotere wens. In de gezamenlijke sessies gebruikt iedereen Kort;
- **de suggestiemodus:** gewone vragen, of bij keuzes twee of drie opties met
  uitleg.

Daarna stelt de skill één vraag per beurt. Echte keuzes verschijnen als
keuzeknoppen als je agent dat ondersteunt, en anders als tekst. Het resultaat is
een `plan-van-aanpak.md`, dat ook in het gesprek staat. Bestudeer het plan, vraag
bij voorkeur een second opinion en geef daarna expliciet opdracht om het uit te
voeren. Pas dan richt de skill je project in volgens de TeamNL-afspraken en
bouwt hij in kleine stappen, met controlemomenten waarop jij meekijkt.

Bekijk de [skillinstructies](.agents/skills/teamnl-agentic-engineering-skill/teamnl-agentic-engineering-skill.md)
en de [versiegeschiedenis](.agents/skills/teamnl-agentic-engineering-skill/CHANGELOG.md).
Meer over starten per agent staat in [docs/agent-startcontrole.md](docs/agent-startcontrole.md).

## Gezamenlijke cursusafspraken

Eigen documenten krijgen kleine letters met streepjes: `plan-van-aanpak.md`
en `agentic-coding-handoff.md`. Vaste namen zoals `AGENTS.md`, `CLAUDE.md`,
`README.md` en `SKILL.md` blijven behouden. Reponamen volgen
`doelgroep-doel-specifiek`, bijvoorbeeld `wsv-data-mining-koffiepauze`.

- `data/example/`: fictieve of aantoonbaar deelbare voorbeelden, elk < 1 MB.
- `data/private/`: echte/lokale data, buiten Git; toegang apart afspreken.
- `docs/handoffs/`: geschoonde sessieverslagen.
- `logs/runtime/` en `logs/test/`: ruwe uitvoerlogs, buiten Git.

De intake legt de data-eigenaar, toestemming, lees- en verwerkingsrechten vast.
Bij Uitgebreid bevat het plan een blok voor het toekomstige `AGENTS.md` plus
voorstellen voor technische toegangsregels; bij Kort staat de kern in het
A4-plan en werkt de bouwagent die bij de start uit in `AGENTS.md`. De intake
wijzigt die instellingen nog niet.

Zie het [naslagwerk](naslagwerk/README.md) en de
[start- en controlehandleiding](docs/agent-startcontrole.md).

## Controle voor de begeleider

- Open `index.html` rechtstreeks, ook zonder internet; controleer de mobiele breedte.
- Wijzig beide velden, sla op en controleer de twee DEMO-waarden in het bestand.
- Probeer lege invoer en aanhalingstekens; beide moeten worden geweigerd.
- Annuleer het opslaanvenster en probeer opnieuw.
- Controleer Chrome/Edge met opslaanvenster en Safari/Firefox met download,
  op de Windows- en macOS-machines die je voor de cursus gebruikt.
- Controleer met bovenstaande Git-commando's dat `.env` genegeerd wordt.

Onderhouders met Node.js kunnen bovendien de automatische checks uitvoeren:

```sh
node --test tests/*.test.cjs
```

Dit is geen vereiste voor cursisten. Tests gebruiken uitsluitend fictieve data.
