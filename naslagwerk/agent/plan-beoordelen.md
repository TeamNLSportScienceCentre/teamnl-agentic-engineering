---
titel: "Een plan beoordelen als je niet alle opties kent"
categorie: grip
moeilijkheid: 2
---

# Een plan beoordelen als je niet alle opties kent

## In één zin
Je hoeft niet alle technieken te kennen om een plan te beoordelen: toets het aan je doel, je grenzen en de vraag hoe je weet dat het werkt.

## Waarom
De TeamNL-skill (`teamnl-agentic-engineering-skill`) maakt een `plan-van-aanpak.md`. Maar hoe weet je of dat plan goed is als je de alternatieven niet kent? En een agent denkt soms maar één kant op. Met vaste vragen en een tweede mening maak je het plan toch beoordeelbaar.

## Wanneer wel, wanneer (nog) niet
Bij de start van een project en bij elke grotere feature. Voor een kleine aanpassing is dit te zwaar.

## Zo begin je
Loop het plan langs met deze vragen:

| Vraag | Waar moet je op letten? |
|---|---|
| Wat is het doel, voor wie? | Concreet en klein genoeg ("weekoverzicht voor 1 coach") |
| Wat valt erbuiten? | Een plan zonder grenzen groeit eindeloos |
| Welke data, en wat mag ermee? | Nepdata voor de agent, afspraken met de data-eigenaar |
| Hoe weet je dat het werkt? | Een controleerbaar resultaat of een [test](../repo/testen.md) |
| Wat is de kleinste eerste stap? | Iets wat je binnen een dag kunt laten zien |
| Wanneer is het af? | Zie [wanneer is het af?](wanneer-is-het-af.md) |

Laat de agent daarna tegenspreken:
> *"Geef twee andere aanpakken voor dit plan, met voor- en nadelen. Welke aannames in het plan zijn het meest riskant?"*

En haal een tweede mening: een collega, of een nieuwe sessie die alleen het plan krijgt (zie [builder / reviewer](builder-reviewer.md)). Leg je keuze vast in `docs/decisions.md`.

## Valkuilen
- Een lang en technisch plan is niet automatisch een goed plan.
- "Branches", "Docker" of "een database" staan erin omdat het kan, niet omdat jouw doel erom vraagt. Vraag bij elk onderdeel: welk probleem lost dit op?
- Een plan is een begin, geen contract: pas het aan als je iets leert, en noteer waarom.

## Zie ook
[`../repo/constitution-specs-taken.md`](../repo/constitution-specs-taken.md) · [`wanneer-is-het-af.md`](wanneer-is-het-af.md) · [`builder-reviewer.md`](builder-reviewer.md) · [`prompten.md`](prompten.md)
