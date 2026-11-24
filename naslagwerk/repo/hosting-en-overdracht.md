---
titel: "Naar de echte wereld: overdracht en hosting"
categorie: draaien
moeilijkheid: 3
---

# Naar de echte wereld: overdracht en hosting

## In één zin
Je project heeft je agent niet meer nodig zodra het af is: het is gewone code die draait zolang de installatie beschreven is, en voor gebruik door anderen kies je samen met de organisatie een plek om het te laten draaien.

## Waarom
"Kan ik het zo opzetten dat ik Claude niet meer nodig heb?" Ja: de agent schrijft code, maar je programma gebruikt de agent niet (tenzij je zelf een AI-dienst in je code aanroept). Wat je wél nodig hebt: een beschrijving hoe het draait, en een plek waar anderen erbij kunnen zonder jouw laptop.

## Wanneer wel, wanneer (nog) niet
- **Overdracht:** altijd, zodra iemand anders je project moet kunnen draaien of onderhouden.
- **Hosting:** pas als het project af is ([wanneer is het af?](../agent/wanneer-is-het-af.md)) en echte gebruikers het nodig hebben. Overleg dan eerst: hosting, toegang en de AVG zijn organisatiekeuzes.

## Zo begin je
**Zonder agent kunnen draaien**
- [ ] [README](readme.md) met installeren en starten, gevolgd door een collega zonder jouw hulp
- [ ] [`requirements.txt`](venv-en-requirements.md) en [`.env.example`](env.md)
- [ ] Werkt op [voorbeelddata](nepdata-maken.md)
- [ ] Eindhand-off: wat werkt, wat niet, wat zou de volgende stap zijn

**Hosting: veelgebruikte vormen** (van licht naar zwaar)
| Vorm | Wanneer | Let op |
|---|---|---|
| Een bestand (PDF, HTML, Excel) dat je script maakt | Een rapport of overzicht | Gedeelde map met de juiste toegang |
| Een script dat een collega zelf draait | Kleine groep, technisch genoeg | README moet kloppen |
| Een interne webapp (bijv. Streamlit of een dashboard) | Coaches willen zelf kijken | Via IT: inloggen, waar staat de data? |
| Container en pipeline | Moet altijd draaien, meerdere onderdelen | Zie [Docker en pipelines](docker-en-yml.md) |

## Valkuilen
- Gratis publieke hosting (zoals GitHub Pages) is openbaar: nooit met atleetdata.
- "Het draait op mijn laptop" is geen hosting: als jij weg bent, is het weg.
- Een app die zelf een AI-model aanroept, heeft wél een account en afspraken nodig, ook na je project.

## Zie ook
[`readme.md`](readme.md) · [`docker-en-yml.md`](docker-en-yml.md) · [`../agent/wanneer-is-het-af.md`](../agent/wanneer-is-het-af.md) · [`../agent/cloud-en-dataplatforms.md`](../agent/cloud-en-dataplatforms.md)
