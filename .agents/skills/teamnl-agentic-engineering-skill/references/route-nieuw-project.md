# Route: nieuw project starten

Gebruik deze route in een basisrepo die nog niet is ingericht, of in een map
zonder TeamNL-basis en zonder werkend project. Er mogen al eigen bestanden
staan, zoals notities, documentatie of een eerste script. Het plan beschrijft het
doel, de eerste bruikbare versie en de inrichting van het project. Na
goedkeuring richt je het project in en bouw je fase 1 in kleine stappen.

**Niet in de basisrepo?** Neem de kern van de basis dan over uit
`assets/templates/`, volgens
[standaardrepo.md](standaardrepo.md#kern-overnemen-buiten-de-basisrepo). Neem
van het geraamte alleen de mappen die het project nodig heeft. Die overname is
een bouwstap in het plan, dus pas na goedkeuring.

De voorbeeldbestanden in de basisrepo laten zien hoe een plan, voorbeelddata en
een map-README eruitzien. Gebruik ze als illustratie van het format. Neem de
fictieve inhoud niet over in het plan van de deelnemer.

## Eigen bestanden

Staan er al eigen bestanden in de map, buiten de basis? Dan zijn die mogelijk
startmateriaal, niet alleen eerder werk. Stel daarover de eerste inhoudelijke
vraag, vóór thema 1:

> Je hebt al drie bestanden klaargezet: `projectnotitie.docx`, `api-uitleg.pdf`
> en `inlezen.py`. Waarvoor zijn ze bedoeld, mag ik ze lezen, en mag ik in het
> plan voorstellen waar ze in de repo komen?

- **Geldt als de vraag van thema 5.** Sla thema 5 daarna over. Bij thema 3 vraag
  je alleen nog naar materiaal en toegang buiten de map.
- **Lezen.** Lees alleen de bestanden waarvoor de gebruiker toestemming geeft.
  Open tijdens de intake geen databestanden of media.
- **Casus al beschreven?** Beschrijft een gelezen document de casus of de
  gebruikers? Vraag bij thema 1 en 2 dan alleen naar wat ontbreekt.
- **Later toegevoegd.** Heeft de gebruiker na het startbeeld nog bestanden in de
  map gezet? Neem die mee in deze vraag.
- **Niets verplaatsen tijdens de intake.** Het plan stelt per bestand een rol en
  een plek voor. Je verplaatst pas na goedkeuring.

Elk eigen bestand krijgt in het plan een van drie rollen:

| Rol | Betekenis | Mogelijke plek |
| --- | --- | --- |
| Startmateriaal | Wordt een gewoon projectbestand | Bijvoorbeeld `docs/project/`, `docs/bronnen/`, `src/` of `data/example/` |
| Referentie | Eerder werk om van te leren, niet om op voort te bouwen | `archive/`, of alleen een verwijzing in het plan |
| Data | Echte gegevens | `data/private/` of goedgekeurde opslag, volgens het risiconiveau |

De gebruiker bepaalt de rol. Bij twijfel stel je referentie voor. Startcode is
nog niet bewezen: fase 1 test die voordat je erop voortbouwt.

Code of eerder werk buiten de map blijft referentie, niet fundament. Neem een
link of locatie op in het plan, of stel voor om het bij de bouw in `archive/` te
zetten.

## De acht thema's

Kort stelt hooguit één brede vraag per thema. Uitgebreid stelt er hooguit drie.
De voorbeeldvragen zijn startpunten, geen checklist. Pas ze aan op wat al bekend
is en sla thema's over die al zijn afgedekt. Thema 8 komt als laatste. In Kort
volgt daarna alleen nog de slotvraag over fase 1, die onder thema 6 valt.

### 1. Casus en aanleiding

Begrijp het probleem, de huidige werkwijze, de aanleiding en de gewenste
verbetering. Een dashboard of model is een mogelijke vorm. Achterhaal de
behoefte die erachter zit.

> Kun je de casus beschrijven: welk probleem wil je oplossen en hoe werk je daar nu mee?

### 2. Gebruikers en beoogd gebruik

Bepaal voor wie de oplossing is, wat die in hun werk moet opleveren en hoe de
deelnemer dat wil bereiken. Een oplossingsrichting mag voorlopig zijn. Leg
vooraf geen stack vast. Bepaal hier ook of er een gebruikersinterface komt. Dat
bepaalt of de TeamNL-stijl van toepassing is.

> Voor wie wil je iets verbeteren, en hoe past de oplossing in hun dagelijkse werk?

### 3. Bronnen, documentatie en voorbeelden

Breng het beschikbare materiaal in kaart en bepaal wat de agent mag raadplegen.
Vraag niet om een technische specificatie. Kies alleen waar het relevant is:

- **API:** staat de documentatie al in de repo, is er een link of moet die nog
  worden opgezocht? Vraag nooit om tokens.
- **Lokale bestanden:** is er een representatief voorbeeld, waar staat het en
  mag de agent het bekijken? Dat een bestand op iemands computer staat, betekent
  niet dat de agent het mag openen.
- **Hardware of andere systemen:** welke toegang en handleidingen zijn er op
  hoofdlijnen?

> Welk materiaal of welke toegang is al beschikbaar om je aanpak uit te werken, en wat moet nog worden geregeld?

Heb je de vraag over eigen bestanden al gesteld? Vraag dan alleen nog naar
materiaal en toegang buiten de map. De limiet geldt voor het hele thema, niet
per bron. Lees alleen materiaal dat
de gebruiker aanwijst en waarvoor toestemming is. Inspecteer geen omliggende
mappen. Open geen API-verbindingen.

### 4. Gegevensbescherming en toegangsgrenzen

Breng gevoeligheid en bescherming samen in één brede vraag.

> Wie bepaalt wat je met de gegevens mag, en welke afspraken gelden voor opslag, verwerking en wat GitHub of de AI-agent mag zien?

Leg per bron vast:

- wie de data-eigenaar of bevoegde beslisser is, en wat die toestaat;
- wat de agent mag lezen;
- wat code lokaal mag verwerken en wie die code uitvoert;
- welke output terug mag naar de agent.

Gebruik daarvoor [data-afspraken.md](data-afspraken.md). Is de toestemming
onbekend? Plan dan met fictieve data. Een onbekende toestemming of gevoeligheid
blijft een voorwaarde vóór gebruik.

Leid uit het antwoord het [risiconiveau](data-afspraken.md#risiconiveau) af:
laag, gevoelig of hoog. Dat kost geen extra vraag. Zet het niveau met de reden
in het plan, als voorstel, en neem de verplichte maatregelen op in de eerste
bouwstap. Twijfel je? Kies dan het hogere niveau.

### 5. Bestaande code en hergebruik

> Is er bestaande code of een eerdere oplossing die we als basis kunnen gebruiken, en waar is die beschikbaar voor de agent?

Heb je de vraag over eigen bestanden al gesteld? Dan is dit thema afgedekt.
Code die nog moet worden aangeleverd, is een afhankelijkheid en nog geen
bewezen basis. Clone, kopieer, migreer of draai geen legacycode tijdens de
intake. Dat kan bij de uitvoering, als het plan dat bevat.

### 6. Aanpak, eerste versie en voorwaarden

Leid de eerste versie af uit de behoeften die al zijn genoemd. Vraag alleen
naar echte keuzes. Noteer op hoofdlijnen:

- hoe bruikbaarheid wordt beoordeeld;
- de belangrijkste randvoorwaarden, zoals lokaal of web, platform,
  besturingssystemen van de gebruikers, installatie en toegang.

> Wat zou een bruikbare eerste stap zijn in jouw aanpak, en wat kan bewust wachten tot later?

**Kort: slotvraag over fase 1.** Stel deze vraag in Kort altijd als laatste, na
thema 8, ook als de deelnemer al een eerste stap noemde. Fase 1 is wat aan het
eind van de eerste bouwsessie moet werken: de MVP.

- Bedenk twee of drie voorstellen. Elk voorstel is een kleine, complete route van
  invoer naar bruikbaar resultaat, die in één sessie haalbaar is.
- Zet het kleinste voorstel dat al waarde heeft als eerste en markeer het als
  aanbevolen. Een eerste stap die de deelnemer al noemde, wordt een van de
  voorstellen.
- Ga uit van fictieve of toegestane data.
- Stel de vraag met de keuzetool.

> Wat moet er aan het eind van de eerste bouwsessie werken? Kies een voorstel of geef je eigen invulling.

Wat buiten fase 1 valt en wanneer fase 1 af is, stel je zelf voor in het plan.

### 7. Logging en beheer

> Wat wil je achteraf kunnen terugvinden over het gebruik en eventuele fouten, en wie beheert die logs?

Heeft de deelnemer geen voorkeur? Stel dan minimale logging voor: fouten en het
resultaat van belangrijke verwerkingen, met tijdstip, onderdeel en status.
`logs/` hoort altijd in het voorstel:

- ruwe logs in `logs/runtime/` en `logs/test/`, buiten Git;
- geschoonde sessieverslagen in `docs/handoffs/`.

Logs bevatten nooit secrets of persoonsgegevens.

### 8. Repository-inrichting en overdracht

> Welke afspraken of voorkeuren heb je voor de indeling en het beheer van de repository, bijvoorbeeld voor code, documenten en bronnen?

- **Reponaam.** Stel een naam voor volgens `doelgroep-doel-specifiek`, in kleine
  letters met streepjes, bijvoorbeeld `wsv-data-mining-koffiepauze`. De naam is
  een voorstel en geen toestemming om een repo aan te maken.
- **Indeling.** Heeft de deelnemer geen voorkeur? Gebruik dan de indeling uit
  [standaardrepo.md](standaardrepo.md) en vraag niet apart om akkoord. De
  basisrepo bevat alle standaardmappen. Stel in het plan voor welke mappen
  blijven en welke weg kunnen, op basis van fase 1 en de bekende vervolgstappen.
- **Uitgebreid.** Bespreek hier zo nodig de Git-werkwijze, de overdraagbaarheid
  en een eventuele deployment.

## Wat het plan bovendien bevat

- **Eigen bestanden.** Staan er eigen bestanden in de map? Neem dan per bestand
  de rol en de voorgestelde plek op, volgens
  [plan-van-aanpak.md](plan-van-aanpak.md).
- **Installatie.** Neem een installatieroute op voor de besturingssystemen uit
  thema 6, volgens [installatie.md](installatie.md).
- **TeamNL-stijl.** Komt er een gebruikersinterface? Neem dan `design.md` en de
  TeamNL-stijl op, volgens [teamnl-stijl.md](teamnl-stijl.md). Zonder interface
  schrijf je 'niet van toepassing'.
- **Agents.** Noteer met welke agents de deelnemer werkt. Daaruit volgen de
  ingangen en instellingen bij de inrichting, zie
  [agent-inrichting.md](agent-inrichting.md). Vraag daar niet apart naar. Is het
  onbekend? Neem het op als open punt.

## Na goedkeuring: inrichten en fase 1 bouwen

Volg [uitvoeren.md](uitvoeren.md). Doorloop de inrichting in deze volgorde, als
eerste bouwstappen van het plan:

1. **Data-afspraken.** Vul het blok Data access in `AGENTS.md` in, met het
   risiconiveau. Richt de toegangsregels en de maatregelen van dat niveau in voor
   de agents die de deelnemer gebruikt. Test ze met fictieve bestanden, met de
   toegangstests die bij het niveau horen. Controleer ook de
   [projectmap-hook](agent-inrichting.md#projectmap-hook-claude-code): draai de
   zelftest en zet de mappen buiten de repo die de deelnemer in thema 3 heeft
   aangewezen, na akkoord, in `.claude/toegestane-mappen.txt`.
2. **Eigen bestanden ordenen.** Alleen als het plan eigen bestanden noemt.
   - **Data.** Vraag de gebruiker om databestanden zelf naar de plek uit het
     plan te verplaatsen, en wacht tot dat klaar is. De toegangsregels blokkeren
     die plek ook voor de agent.
   - **Startmateriaal en referentie.** Verplaats die zelf naar de plek uit het
     plan. Staat de map in Git? Gebruik dan `git mv`, zodat de geschiedenis
     meegaat. Zonder Git legt de tabel in het plan vast wat waarheen ging. Pas
     verwijzingen in code aan als een pad verandert.
   - **Secrets.** Zie je in startcode een sleutel of wachtwoord? Toon het niet,
     vervang het door een verwijzing naar `.env` en meld dat de gebruiker het
     secret moet vervangen.
   - **Niets verwijderen.** Een bestand zonder rol blijft staan en wordt een open
     punt.
3. **Projectdocumenten.** Vervang de basis-README door de projectREADME uit
   `assets/templates/README.md`. Vul `.gitignore` aan voor de gekozen stack.
   Houd `.env.example` alleen als het project configuratie of secrets nodig heeft,
   en vul het met de echte variabelen, zonder waarden.
4. **Structuur.** Houd de mappen die het plan noemt. Verwijder de andere mappen
   uit het geraamte, inclusief hun README, maar nooit een map waarin nog een
   eigen bestand staat. Werk de README van elke map die blijft bij als het
   project iets anders nodig heeft.
5. **Omgeving en installatie.** Leg de afhankelijkheden reproduceerbaar vast en
   gebruik waar het past een aparte projectomgeving, zoals een venv bij Python.
   Vervang de voorbeeldstap in de installatiescripts door de echte stappen.
   Verwijder de scripts voor systemen die niemand gebruikt. Test de route.
6. **Stijl.** Bij een interface: vul de projectnaam in `design.md` in en zet
   alleen geverifieerde assets in `assets/brand/`. Zonder interface: verwijder
   `design.md` en `assets/`.
7. **Basisresten opruimen.** Verwijder of vervang de voorbeeldbestanden die in
   [standaardrepo.md](standaardrepo.md#voorbeeldbestanden-in-de-basis) staan.
   De geschiedenis van de basis staat in de CHANGELOG van de skill.
8. **AGENTS.md afronden.** Zet de status op 'ingericht'. Vul het doel, het actieve
   plan, het start- en testcommando en de Git-werkwijze in. Behoud de regel met
   de basisversie.

Bouw daarna fase 1 in de stappen uit het plan. Plaats bij de bouw ook de
coderegel uit het [watermerkje](plan-van-aanpak.md#watermerkje), tenzij de
deelnemer dat niet wil.
