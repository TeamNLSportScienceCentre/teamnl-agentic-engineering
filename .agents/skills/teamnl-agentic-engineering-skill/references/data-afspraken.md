# Data-afspraken

Er is geen universele datatoegang. De intake legt per project vast welke gegevens
er zijn, wie over het gebruik beslist, waar ze staan en wat de agent mag lezen of
laten verwerken. Ook de toegestane uitvoer, logs en foutmeldingen horen bij die
afspraak. Bij een feature hergebruik je de bestaande afspraken en bespreek je
alleen wat verandert.

## Lezen of laten verwerken

Wat de agent leest, gaat naar de modelaanbieder. Laat de agent een script
schrijven dat de data lokaal verwerkt? Dan ziet het model alleen wat het script
teruggeeft. Houd die uitvoer daarom klein en niet herleidbaar. Geef aantallen,
kolomnamen en samenvattende statistieken. Geef geen rijen of losse waarden.
Noem in foutmeldingen het rijnummer en de kolom, niet de waarde. Hoe je dat in
de code afdwingt, staat in [veilig-verwerken.md](veilig-verwerken.md).

## Wat je vastlegt

| Onderwerp | De vraag die beantwoord moet zijn |
| --- | --- |
| Bron en bevoegdheid | Welke bron is het, wie is de eigenaar en welke toestemming geldt voor dit gebruik? |
| Risiconiveau | Is het risico laag, gevoelig of hoog, en waarom? Zie [Risiconiveau](#risiconiveau). |
| Leesrechten | Welke locaties mag de agent lezen en welke zijn uitgesloten? |
| Verwerking en uitvoer | Wie draait de code, en welke resultaten mogen terug naar de agent? |
| Technische inrichting | Welke instellingen en hooks zijn actief voor deze agent, deze versie en deze omgeving? |
| Controle en beperkingen | Welke toegestane en verboden acties zijn getest met fictieve bestanden, en wat blijft onbekend? |

Vraag wie namens de data-eigenaar mag beslissen, bijvoorbeeld de sporter, de
bond, de data-aanbieder of de privacy officer. Vraag nooit naar namen van
individuele sporters of naar ruwe records.

Een bestand op een laptop is niet automatisch deelbaar met een AI-aanbieder.
Daarnaast gelden drie wettelijke en contractuele punten:

- Gezondheidsgegevens van sporters zijn bijzondere persoonsgegevens onder de AVG.
- Gelicentieerde data mag vaak niet aan derden worden verstrekt.
- Een AI-aanbieder is een derde.

Is de toestemming onbekend? Dan blijft het gebruik van echte data geblokkeerd.
Plannen en bouwen met fictieve voorbeelden kan wel.

## Risiconiveau

Het risiconiveau bepaalt welke maatregelen verplicht zijn. Je leidt het af uit
het antwoord op de datavraag, dus het kost geen extra vraag. Bepaal het per
project en opnieuw bij elke nieuwe bron.

- **In het plan.** Zet het niveau in het plan als voorstel, met de reden. De
  gebruiker kan het bijstellen.
- **Twijfel.** Twijfel je tussen twee niveaus? Kies dan het hogere.
- **Verlagen.** Een lager niveau kan alleen met akkoord van de gebruiker. Leg de
  reden vast in `docs/decisions.md`.
- **Nog onbekend.** Is nog niet bekend welke data er komt? Werk dan alleen met
  fictieve data. Bepaal het niveau voordat er echte data in het project komt.

| Niveau | Voorbeelden |
| --- | --- |
| Laag | Openbare data, fictieve data, cijfers waarin geen personen te herkennen zijn |
| Gevoelig | Persoonsgegevens zoals namen en contactgegevens; prestatie- en trainingsgegevens van sporters; gelicentieerde data |
| Hoog | Identiteitsbewijzen zoals paspoort, ID-kaart en rijbewijs; BSN; gezondheids- en medische gegevens, zoals hartslag, slaap en blessures; biometrie; financiële gegevens; persoonsgegevens van minderjarigen |

Verplichte maatregelen per niveau:

| Maatregel | Laag | Gevoelig | Hoog |
| --- | --- | --- | --- |
| Opzet (zie hieronder) | Elke opzet | Nepdata, blind bouwen, sample met toestemming, of lokaal verwerken met begrensde uitvoer | Alleen blind bouwen of nepdata. De agent draait geen code op echte data; dat doet de gebruiker. |
| Plek van echte data | `data/private/` | `data/private/` of buiten de repo | Buiten de repo, en buiten mappen die naar de cloud synchroniseren, zoals OneDrive, iCloud of Dropbox, tenzij de data-eigenaar die opslag goedkeurt. Dat geldt ook voor uitvoer en logs van echte runs: `DATA_DIR`, `OUTPUT_DIR` en `LOG_DIR` in `.env`. |
| Leesblokkades en hooks | De basis: leesblokkades en de projectmap-hook in `.claude/settings.json` | De basis | De sjablonen voor hoog: uitgebreide leesblokkades en de beschermhook voor Claude Code, Codex, GitHub Copilot en Mistral Vibe. Zie [agent-inrichting.md](agent-inrichting.md#bescherming-bij-risiconiveau-hoog). |
| Code | Geen extra eisen | Foutmeldingen zonder waarden; alleen samenvattingen terug naar de agent | Daarnaast de echte-data-sleutel, paden via configuratie, een logfilter en een lektest. Zie [veilig-verwerken.md](veilig-verwerken.md). |
| Toegangstests ([agent-inrichting.md](agent-inrichting.md#toegangsgrenzen-testen)) | 1 tot en met 3 | 1 tot en met 4 | 1 tot en met 5 |
| Git | Gitleaks met de standaardregels | Gitleaks met de standaardregels | Daarnaast `.gitleaks.toml` met regels voor persoonsnummers |

Bij hoog richt je de beschermhook in voor elke agent die in het project wordt
gebruikt. Een agent waarvan de hook nog niet actief is, of waarvoor de
toegangstests niet slagen, gebruik je niet in dit project. Noteer dat in
`AGENTS.md` en `docs/agent-startcontrole.md`.

## Opzetten om uit te kiezen

Welke opzet past, hangt af van het risiconiveau.

| Opzet | Wat gaat naar het model? | Geschikt voor |
| --- | --- | --- |
| Blind bouwen: de agent krijgt alleen het schema, de gebruiker draait de code en geeft fouten door | Schema en wat de gebruiker doorgeeft | Zeer gevoelige data |
| Bouwen op nepdata: de agent maakt synthetische data en ontwikkelt daarop | Nepdata en uitvoer daarop | **Aanbevolen startpunt** |
| Sample met toestemming | Een paar echte, liefst gepseudonimiseerde rijen | Rommelige data waarbij een schema niet genoeg zegt |
| Lokaal verwerken: de agent schrijft en draait scripts op echte data, maar opent die niet zelf | Alleen de begrensde uitkomst | Gevoelige data, als de uitvoer klein blijft |
| Volledige data delen | Alles | Openbare data, of met expliciete toestemming van de eigenaar |

Bij een externe API met persoonsgegevens geldt vaak: 'de gebruiker draait het
live'. De agent leest dan geen `.env` en doet zelf geen API-calls. Hij
ontwikkelt met gemockte antwoorden. Moet de gebruiker een call uitvoeren? Dan
beschrijft de agent per call wat die doet, wat je kunt verwachten en wat de
risico's zijn. De gebruiker geeft alleen een geschoonde samenvatting terug.

## Blok voor AGENTS.md

Vul dit blok in het plan in. Bij de inrichting neem je het over in `AGENTS.md`.
Wordt het te groot, bijvoorbeeld bij meerdere bronnen? Laat de kernregels dan in
`AGENTS.md` staan en zet de details per bron in `docs/data-afspraken.md`.

```markdown
## Data access
- Data-eigenaar/bevoegde rol: [rol]. Toestemming: [omvang of nog te regelen].
- Risiconiveau: [laag / gevoelig / hoog], omdat [reden].
- Opzet: [blind bouwen / nepdata / sample met toestemming / lokaal verwerken / volledige data].
- Uitvoering: [gebruiker / agent lokaal / afgeschermde omgeving].
- Echte data: [data/private/ | buiten de repo via DATA_DIR, OUTPUT_DIR en LOG_DIR in .env].
- Agent mag lezen: [concrete toegestane paden en soorten informatie].
- Agent mag niet lezen, printen of uploaden: .env en varianten (behalve .env.example
  met fictieve waarden), data/private/, media/private/, [bij hoog ook output/,
  logs/runtime/, tmp/ en de externe datamap], [overige paden].
- Lokaal verwerken van echte data: [niet toegestaan / expliciet afgesproken scope].
- Ontwikkel en test met fictieve data in data/example/; elk bestand < 1 MB.
- Uitvoer naar de agent: alleen goedgekeurde, niet-herleidbare samenvattingen; geen
  echte rijen, secrets of waarden in foutmeldingen, logs, notebooks of exports.
- Technische toegangsregels: [agent, configuratieplek, verboden paden, teststatus
  en datum]. Zie docs/agent-startcontrole.md.
- Zolang toestemming of technische bescherming onduidelijk is: alleen fictieve data.
- Wijzigingen aan deze grenzen: alleen zichtbaar voorgesteld en na akkoord.
```

## Van afspraak naar controleerbare inrichting

`AGENTS.md` beschrijft de afspraken en verwijst naar de concrete instellingen en
hooks. Een bestand met instructies bewijst niet dat de toegang technisch is
geblokkeerd. Bij de uitvoering doorloop je daarom vier stappen:

1. **Instellingen en hooks inrichten** voor de agents die de gebruiker gebruikt,
   volgens [agent-inrichting.md](agent-inrichting.md). Gebruik bij risiconiveau
   hoog de sjablonen uit `assets/templates/hoog-risico/`.
2. **Testen met fictieve bestanden.** Voer de toegangstests uit
   [agent-inrichting.md](agent-inrichting.md#toegangsgrenzen-testen) uit. Het
   risiconiveau bepaalt welke tests verplicht zijn. Test nooit met echte
   gevoelige data.
3. **Uitkomst vastleggen** in `docs/agent-startcontrole.md`: wat werkt, wat niet
   is geblokkeerd en wat onbekend blijft. Noem de agent, de versie en de datum.
4. **Harde isolatie.** Bij risiconiveau hoog is dit verplicht, bij de andere
   niveaus kies je het als de agent echt niet bij de data mag kunnen.
   - Zet de echte data, en de uitvoer en logs van echte runs, buiten de omgeving
     waartoe de agent toegang heeft.
   - Gebruik daarvoor `DATA_DIR`, `OUTPUT_DIR` en `LOG_DIR` in `.env`, met een
     map buiten de repo, of een sandbox zonder die data.
   - Kies geen map die naar de cloud synchroniseert, zoals OneDrive, tenzij de
     data-eigenaar die opslag goedkeurt.

   Een leesblokkade is geen kluis: een script dat de agent draait, kan het
   bestand vaak nog openen.

De standaard geeft geen algemene veiligheidsgarantie. De dekking van hooks,
permissies en isolatie verschilt per agent, versie en omgeving.

## Git, secrets en opschonen

- **`.gitignore`** bepaalt welke niet-gevolgde bestanden Git negeert. Het is geen
  toegangsregeling voor de agent. Het verwijdert ook niets uit bestaande commits.
- **Gitleaks vóór een commit.** Het bestand `.pre-commit-config.yaml` laat
  Gitleaks gestaagde wijzigingen controleren. Activeer dat eenmalig per computer
  met `pre-commit install`. De standaardregels van Gitleaks herkennen patronen
  van secrets, maar geen persoonsgegevens. Bij risiconiveau hoog komt daarom
  `.gitleaks.toml` erbij, met regels voor paspoort-, ID- en BSN-nummers. Het
  sjabloon staat in `assets/templates/hoog-risico/`.
- **Secrets.** Echte sleutels blijven buiten Git. Deel alleen een
  `.env.example` zonder geheime waarden.
- **Opschonen.** Schoon logs, notebook-output en handoffs op voordat inhoud via
  een agent of via Git wordt gedeeld.

**Agenthooks en Git-hooks** hebben elk een eigen doel. Een agenthook grijpt in
vóór of na een handeling van de agent, bijvoorbeeld een poging om `.env` te
lezen. Een Git-hook, zoals de Gitleaks-controle, grijpt in vóór een commit,
ongeacht wie die commit maakt. Beschrijf ze in de projectdocumentatie
afzonderlijk.
