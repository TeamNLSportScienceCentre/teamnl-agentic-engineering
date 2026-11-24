# Uitvoeren na goedkeuring

Je begint pas met uitvoeren nadat de gebruiker het plan heeft gelezen en
expliciet opdracht geeft om het uit te voeren. Zet in het plan de status op
`goedgekeurd op YYYY-MM-DD` en zodra je begint op `in uitvoering`.

## Vóór de eerste stap

- **Oriënteren.** Lees het plan, `AGENTS.md`, `docs/decisions.md` en de
  nieuwste handoff.
- **Werkstaat.** Bekijk de status van de werkmap, bijvoorbeeld met
  `git status`. Staan er wijzigingen die niet van jou zijn? Meld die dan en
  vraag of je eromheen moet werken. Ruim ze niet zelf op.
- **Eerst de data-afspraken.** Is een stap afhankelijk van data-afspraken of
  toegangsregels? Richt die dan eerst in, met de maatregelen van het
  risiconiveau, en controleer ze. Zie [data-afspraken.md](data-afspraken.md),
  [agent-inrichting.md](agent-inrichting.md) en
  [veilig-verwerken.md](veilig-verwerken.md).
- **Toegang.** Ontbreekt noodzakelijke toegang of toestemming? Voer dan alleen
  de stappen uit die daar niet van afhangen. Meld wat de gebruiker moet regelen.

## Per bouwstap

1. **Aankondigen.** Zeg in één of twee zinnen wat je gaat doen en welke
   bestanden je verwacht te wijzigen.
2. **Uitvoeren.** Houd de wijziging klein en binnen de stap.
3. **Controleren.**
   - Maak en draai passende automatische tests, met fictieve data.
   - Draai bestaande tests opnieuw. Bij risiconiveau hoog hoort de lektest
     daarbij. Faalt die? Herstel dan eerst het lek.
   - Zet ruwe testuitvoer in `logs/test/` als die bewaard moet worden.
   - Rapporteer alleen een geschoonde samenvatting.
4. **Afvinken.** Vink de stap af in het plan en meld kort het resultaat en
   eventuele beperkingen.
5. **Controlemoment.** Stop bij elk afgesproken controlemoment. Laat de
   gebruiker kijken of bijsturen en wacht op een expliciet 'ga door'.

Je stelt geen terugkerende verplichte testvragen. De gebruiker test het gebruik
zelf, toetst het resultaat aan de minimale vereisten en geeft bevindingen terug.
Verwerk die bevindingen als aanpassing of extra stap in hetzelfde plan.

## Grenzen tijdens de uitvoering

- **Binnen het plan blijven.** Is iets nodig dat niet in het plan staat? Stop
  dan en stel een aanpassing van hetzelfde plan voor. Werk het plan pas na
  akkoord bij en ga daarna verder. Een nieuwe feature krijgt een eigen plan.
- **Toegangsgrenzen.** Verruim een toegangsgrens nooit stilzwijgend, ook niet om
  iets werkend te krijgen. Stel een wijziging zichtbaar voor met de reden en het
  risico. Leg die na akkoord vast in `AGENTS.md` en `docs/decisions.md`. Test de
  nieuwe grens opnieuw.
- **Installeren.** Iets installeren of buiten de repository wijzigen doe je
  alleen na een overzicht vooraf en akkoord, volgens
  [installatie.md](installatie.md). Dat geldt ook voor ontbrekende
  basisprogramma's.
- **Git.**
  - Volg de Git-werkwijze uit `AGENTS.md` of `docs/decisions.md`.
  - Is die niet vastgelegd? Commit of push dan alleen als de gebruiker daarom
    vraagt.
  - Gebruik nooit `git add -f` voor genegeerde bestanden.
  - Gebruik nooit `--no-verify` om de controle op secrets over te slaan.
- **Twee mislukte pogingen.** Lukt iets na twee pogingen niet? Stop dan,
  beschrijf wat je hebt geprobeerd en stel een andere aanpak voor.

## Projectafspraken bijhouden

| Bestand | Wanneer bijwerken | Inhoud |
| --- | --- | --- |
| `AGENTS.md` | Bij de start en bij relevante uitbreidingen | Actuele werkafspraken; de verwijzing naar het actieve plan; data-afspraken; start- en testcommando's; de basisversie. Houd het compact en verwijs naar details. |
| `README.md` | Als installeren, starten, gebruiken, controleren of benodigde toegang verandert | Uitleg voor mensen, met exacte commando's |
| `docs/decisions.md` | Na een goedgekeurde, belangrijke keuze | Het besluit, de reden, de gevolgen en de status. Stel voor, laat goedkeuren en leg dan vast. |
| `docs/handoffs/` | Aan het eind van elke werksessie | Een geschoonde handoff volgens `assets/templates/handoff.md` |
| `docs/architecture.md` | Alleen als de opbouw uitleg nodig heeft | De actuele uitleg van de architectuur |
| Het plan | Na elke stap, en bij wijzigingen na akkoord | Vinkjes, status en bijgewerkte inhoud |

Een handoff is geschiedenis, een beslissing is de actuele stand. Zet een
beslissing dus niet alleen in een handoff.

## Een werksessie afsluiten

Schrijf de handoff in `docs/handoffs/YYYY-MM-DD-HHMM-onderwerp.md`. Gebruik
daarvoor de tijd op het moment van schrijven. De handoff bevat:

- wat er is gedaan en welke stappen zijn afgevinkt;
- welke controles zijn uitgevoerd, met het resultaat;
- beslissingen en open punten;
- beperkingen;
- de volgende stap.

Schoon de handoff, logs en notebook-output op voordat je inhoud deelt met een
agent of via Git. Er komen geen secrets, persoonsgegevens, echte datarijen of
ruwe uitvoer in.

Controleer daarna of `AGENTS.md` nog naar het juiste actieve plan verwijst. Een
nieuwe sessie moet via `AGENTS.md` het actieve plan, de beslissingen en de
laatste handoff kunnen vinden.

## Hervatten in een nieuwe sessie

1. Lees `AGENTS.md`, het actieve plan, `docs/decisions.md` en de nieuwste handoff.
2. Vat in twee of drie zinnen samen waar het werk staat en wat de volgende stap
   is.
3. Ga pas verder als de gebruiker dat bevestigt. Een eerdere goedkeuring van het
   plan blijft gelden voor de stappen die nog openstaan, maar het hervatten van
   een sessie bevestig je kort.

## Afronden

Zijn alle stappen afgevinkt en zijn de minimale vereisten door de gebruiker
getoetst?

- Zet het plan op `afgerond op YYYY-MM-DD`.
- Werk `AGENTS.md` bij.
- Schrijf een handoff.
- Bied waar dat past de volgende route aan, bijvoorbeeld een nieuwe feature.
