---
titel: "Testen: hoe weet je dat het werkt?"
categorie: kwaliteit
moeilijkheid: 2
---

# Testen: hoe weet je dat het werkt?

## In één zin
Een test is een klein stukje code dat automatisch controleert of je project nog doet wat je verwacht, zodat je het merkt als een wijziging van jou of je agent iets kapotmaakt.

## Waarom
Een agent past snel veel code aan. Zonder tests ontdek je pas na weken dat een berekening ongemerkt veranderd is. Tests zijn ook een manier om je agent te controleren zonder elke regel te lezen: *"draait alles nog groen?"*

## Wanneer wel, wanneer (nog) niet
- **Wel:** voor de berekeningen waar het om draait (belasting, zones, piekprestaties), voor code die een coach of collega gebruikt, en na elke fout die je hebt opgelost.
- **Nog niet:** voor een plotje dat je één keer bekijkt, of code die je morgen weggooit.

## Zo begin je
Je hoeft niet zelf tests te verzinnen voor elk geval. Deze soorten werken goed voor data-analyse:

| Soort test | Voorbeeld |
|---|---|
| **Bekend antwoord** | Drie verzonnen trainingen van 60, 90 en 30 minuten → totaal 180 |
| **Grenzen** | Hartslag tussen 30 en 230; geen negatieve afstanden |
| **Vorm** | De uitvoer heeft de kolommen `datum`, `atleet_id`, `belasting` |
| **Randgevallen** | Een lege week, één ontbrekende meting, een sprinter én een duursporter |
| **Na een fout** | De fout die je net oploste, komt niet terug |

Met `pytest` ziet een test er zo uit (`tests/test_belasting.py`):
```python
from src.belasting import weekbelasting

def test_totaal_van_drie_trainingen():
    assert weekbelasting([60, 90, 30]) == 180
```
Draaien: `python -m pytest`. Vraag je agent:
> *"Stel tests voor de belangrijkste berekening voor. Leg per test uit welke fout hij zou vangen. Schrijf ze pas als ik akkoord ben."*

Lees die uitleg kritisch: denk je aan een fout die nergens getest wordt? Vraag erom.

## Valkuilen
- Een agent die een falende test "oplost" door de test aan te passen. Kijk naar de diff.
- Tests op echte data. Gebruik [voorbeelddata](nepdata-maken.md) zodat iedereen (en de agent) ze kan draaien.
- Alleen testen wat makkelijk is. De belangrijkste vraag: welke fout zou het meest schadelijk zijn?

## Zie ook
[`nepdata-maken.md`](nepdata-maken.md) · [`../agent/debuggen.md`](../agent/debuggen.md) · [`../agent/grip-op-agentcode.md`](../agent/grip-op-agentcode.md) · [`folder-structure.md`](folder-structure.md)
