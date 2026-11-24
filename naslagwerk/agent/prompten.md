---
titel: "Effectief prompten: slimme trucs"
categorie: hoe-werk-je-samen
moeilijkheid: 1
---

# Effectief prompten: slimme trucs

## In één zin
Geef je agent wat een nieuwe collega nodig heeft: doel, context, grenzen en hoe je weet dat het goed is, en laat hem eerst vragen stellen of een plan maken.

## Waarom
De agent weet alleen wat in je prompt, je map en je `AGENTS.md` staat. Een vage vraag geeft een gok. Een goede opdracht scheelt rondes heen en weer, en dus tijd en tokens.

## Wanneer wel, wanneer (nog) niet
Altijd. Voor een kleine vraag is één zin genoeg; voor een feature loont een goede opdracht.

## Zo begin je
**Een goede opdracht heeft vier delen:**
1. **Doel:** wat moet er aan het eind zijn, voor wie? *"Een weekoverzicht van trainingsbelasting voor de coach."*
2. **Context:** welke bestanden, welke data? Verwijs naar bestanden (vaak met `@bestandsnaam`).
3. **Grenzen:** wat mag niet? *"Alleen `data/example/`, geen nieuwe packages zonder te vragen."*
4. **Klaar als:** *"Het script draait op de voorbeelddata en maakt `output/week.png`."*

**Trucs die werken**
| Truc | Voorbeeld |
|---|---|
| Laat eerst vragen stellen | *"Stel me eerst vragen, één per keer, voordat je begint."* |
| Eerst een plan | *"Maak een plan. Nog niet coderen."* (planmodus) |
| Vraag om alternatieven | *"Geef twee andere aanpakken met voor- en nadelen."* (tegen het één-kant-op-denken) |
| Laat uitleggen | *"Leg uit wat je gedaan hebt alsof ik geen programmeur ben."* |
| Laat controleren | *"Hoe kan ik zelf zien dat dit klopt?"* |
| Herbruik goede prompts | Zet terugkerende instructies in `AGENTS.md` of een [skill](../repo/skills.md) |

## Valkuilen
- Alles in één prompt ("bouw het dashboard met login en export"). Knip het op.
- Afspraken alleen in de chat: de volgende sessie is ze kwijt. Zet ze in `AGENTS.md`.
- Echte data in je prompt plakken. Beschrijf de kolommen, of gebruik [nepdata](../repo/nepdata-maken.md).

## Zie ook
[`workflow.md`](workflow.md) · [`plan-beoordelen.md`](plan-beoordelen.md) · [`../repo/agents-md.md`](../repo/agents-md.md) · [`../repo/skills.md`](../repo/skills.md)
