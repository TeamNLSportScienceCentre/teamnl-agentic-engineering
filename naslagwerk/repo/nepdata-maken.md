---
titel: "Nepdata maken"
categorie: veilig
moeilijkheid: 1
---

# Nepdata maken

## In één zin
Laat je agent een script schrijven dat realistische, maar volledig verzonnen voorbeelddata maakt op basis van alleen de kolomnamen en de verwachte waarden.

## Waarom
Met nepdata kan je agent alles bouwen en testen zonder ooit je echte (atleet)data te zien. Je buddy kan je project direct draaien, en je kunt het veilig delen. Het is het aanbevolen startpunt uit sessie 1.

## Wanneer wel, wanneer (nog) niet
- **Wel:** altijd als je echte data gevoelig is, of als een ander je project moet kunnen draaien.
- **Minder nodig:** je data is openbaar (bijvoorbeeld uitslagen die al online staan). Controleer dat met de data-eigenaar.

## Zo begin je
1. **Beschrijf de data, niet de inhoud:** kolomnamen, eenheden en realistische bereiken. Bijvoorbeeld:
   `datum` (2026-01-01 t/m 2026-03-31), `atleet_id` (A01–A08), `duur_min` (20–150), `hartslag_gem` (110–175).
2. **Vraag de agent:**
   > *"Schrijf `scripts/maak_voorbeelddata.py` dat met een vaste seed een klein CSV-bestand maakt in `data/example/` met deze kolommen en bereiken. Voeg ook een paar randgevallen toe: een ontbrekende meting en een lege week."*
3. **Draai het script** en bekijk het resultaat: lijkt het genoeg op de echte data om je code te testen?
4. **Commit** het script én het kleine voorbeeldbestand (< 1 MB). Zet in de README hoe je het opnieuw maakt.

## Valkuilen
- **Nepdata afleiden van echte rijen** (echte data "een beetje aanpassen") is geen nepdata. Alleen namen weghalen maakt data niet anoniem.
- Te nette nepdata: echte data heeft gaten, uitschieters en tikfouten. Voeg die bewust toe, anders faalt je code pas op de echte data.
- Geen vaste seed: dan krijg je elke keer andere data en zijn je [tests](testen.md) niet stabiel.

## Zie ook
[`data-folders.md`](data-folders.md) · [`../agent/data-access.md`](../agent/data-access.md) · [`testen.md`](testen.md) · [`../agent/hooks.md`](../agent/hooks.md)
