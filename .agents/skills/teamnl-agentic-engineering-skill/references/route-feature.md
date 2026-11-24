# Route: nieuwe feature ontwikkelen

Gebruik deze route voor een verandering in een repository die al is ingericht,
met projectafspraken in `AGENTS.md`. Een feature hergebruikt de bestaande
inrichting en afspraken. Je doorloopt de inrichting niet opnieuw.

Mist de repository de basis, zoals `AGENTS.md`, data-afspraken of een
README? Zeg dat in één zin en adviseer eerst de route Bestaande repo op orde
brengen. De gebruiker beslist. Kiest die voor de feature, noteer de ontbrekende
basis dan als open punt.

## Eerst lezen

Lees deze bestanden en stel daarna je eerste vraag:

- `AGENTS.md`, inclusief de data-afspraken;
- het projectplan;
- `docs/decisions.md`;
- de nieuwste handoff in `docs/handoffs/`;
- bestaande featureplannen in `specs/` die raakvlakken hebben;
- de code die de feature waarschijnlijk raakt.

Neem bekende keuzes en antwoorden over.

## Kort: hooguit vijf vragen

De korte feature-intake telt hooguit vijf vragen in totaal. Keuzevragen en
verduidelijkingen tellen mee. Stel één vraag per beurt. Minder vragen mag. Voeg
geen aparte verplichte keuzeronde toe.

De vijf onderwerpen hieronder zijn mogelijkheden, geen verplichte lijst.
Combineer of sla over wat al bekend is.

1. **Gewenste verandering.** Wat wil je aanpassen en wat moet dat de gebruiker
   opleveren?
2. **Afbakening.** Wat hoort bij deze feature en wat laten we voor later?
3. **Minimale vereisten.** Wat moet de feature minimaal kunnen om voor jou
   bruikbaar te zijn?
4. **Randvoorwaarden.** Welke nieuwe bronnen, koppelingen of veranderingen in
   datatoegang zijn nodig?
5. **Uitvoering en regie.** In welke kleine stappen pakken we dit aan, en
   wanneer wil je zelf meekijken of bijsturen?

Ook na vijf vragen kan iets onbeantwoord blijven. Neem dat zichtbaar op als open
punt. Ontbreekt noodzakelijke toegang of toestemming? Vermeld dan wat eerst
geregeld moet worden. Vraag niet verder om de korte variant alsnog volledig te
maken.

Staat de suggestiemodus aan? Dan mag een vraag opties bevatten, bijvoorbeeld
voor de afbakening of de aanpak. Uitleg op verzoek telt niet als extra vraag.
Voeg in Kort geen Git-keuzes toe. De enige uitzondering is een feature die iets
nieuws en gevoeligs ontwikkelt, zoals credentials of persoonsgegevens.

## Uitgebreid: voor een grotere verandering

Uitgebreid is bedoeld voor een wens die meerdere onderdelen raakt. Je verheldert
drie dingen: wat eronder valt, welke onderdelen worden geraakt en hoe je het
uitvoerbaar maakt. De omvang van de verandering bepaalt hoeveel verdieping nodig
is. Het is geen standaard technisch interview.

- Gebruik de vijf onderwerpen hierboven. Voeg een zesde onderwerp toe:
  **Git-werkwijze**, bijvoorbeeld een branch per feature, commits per stap of
  een review. Sla dat zesde onderwerp over als de werkwijze al in `AGENTS.md` of
  `docs/decisions.md` staat.
- Stel hooguit drie vragen per onderwerp, één per beurt. Stop zodra het
  onderwerp duidelijk genoeg is om te plannen.
- Breng in het plan de samenhang tussen de onderdelen in beeld. Noem
  alternatieven en aannames.

Je mag Uitgebreid adviseren. Bijvoorbeeld:

> Je wens lijkt meerdere onderdelen te raken. De uitgebreide intake kan helpen om die samenhang en de stappen helder te krijgen. Je kunt ook kiezen voor de korte variant.

## Plan en locatie

Bewaar het plan in `specs/<feature>/plan-van-aanpak.md`.

- **Featurenaam.** Gebruik kleine letters en streepjes, bijvoorbeeld
  `specs/sprint-export/`.
- **Bestaand pad.** Bestaat het pad al voor een andere feature? Kies dan een
  andere naam en meld die.
- **Verdieping.** Een verduidelijking of verdieping werkt hetzelfde plan bij.
- **Nieuwe feature.** Een nieuwe feature krijgt een eigen map.

Gebruik het sjabloon 'Feature' uit [plan-van-aanpak.md](plan-van-aanpak.md).
Ook een grote feature houdt één plan, met meerdere kleine bouwstappen. Houd de
inhoud van de feature zoveel mogelijk in het featureplan. In `AGENTS.md` komt
alleen de verwijzing naar het actieve plan.

## Data en toegang

Bestaande grenzen blijven gelden totdat een wijziging expliciet is afgesproken.
Heeft de feature nieuwe bronnen of andere datatoegang nodig? Leg die afspraken
dan vast in het plan, volgens [data-afspraken.md](data-afspraken.md). Bij de
uitvoering richt je de instellingen in en controleer je ze, vóór het werk dat
ervan afhangt. Verruim een grens nooit om de feature werkend te krijgen.

Het [risiconiveau](data-afspraken.md#risiconiveau) van het project blijft
gelden. Brengt de feature gevoeligere data binnen, bijvoorbeeld gezondheids- of
identiteitsgegevens? Verhoog het niveau dan in het plan, zonder extra vraag. Zet
de extra maatregelen in de eerste bouwstappen, vóór het werk met die data.

## Na goedkeuring

Volg [uitvoeren.md](uitvoeren.md). Werk het plan stap voor stap af en stop op de
controlemomenten die met de gebruiker zijn afgesproken. Is de feature af? Dan
toetst de gebruiker het resultaat aan de minimale vereisten. Zet de verwijzing
in `AGENTS.md` terug naar het projectplan of naar het volgende actieve plan.
