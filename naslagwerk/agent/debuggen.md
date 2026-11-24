---
titel: "Fouten oplossen met je agent"
categorie: grip
moeilijkheid: 1
---

# Fouten oplossen met je agent

## In één zin
Laat de agent eerst de oorzaak uitleggen en pas daarna één gerichte oplossing maken, op nepdata en zonder echte data in de foutmelding.

## Waarom
Een agent "repareert" graag snel, soms door het symptoom weg te poetsen of door drie dingen tegelijk te veranderen. Dan werkt het misschien, maar weet niemand waarom, en komt de fout later terug.

## Wanneer wel, wanneer (nog) niet
Bij elke foutmelding of elk vreemd resultaat. Kleine typfouten kun je ook zelf oplossen.

## Zo begin je
1. **Maak de fout reproduceerbaar,** het liefst op [voorbeelddata](../repo/nepdata-maken.md): *"Bij `python src/analyse.py` met `data/example/` krijg ik deze fout: …"*
2. **Geef de hele foutmelding,** maar controleer eerst of er geen echte data in staat (namen, waarden, paden). Haal die eruit.
3. **Eerst de oorzaak:** *"Leg uit wat de oorzaak is. Nog niets aanpassen."*
4. **Dan één oplossing:** *"Los alleen deze oorzaak op, in zo min mogelijk regels."* Kijk naar de diff.
5. **Voorkom herhaling:** *"Schrijf een test die deze fout had gevangen."* Zie [testen](../repo/testen.md).
6. **Commit** de oplossing met een bericht dat de oorzaak noemt.

Lukt het na twee pogingen niet? Begin een **nieuwe chat** met een korte samenvatting: wat je doet, wat je verwacht, wat er gebeurt en wat al geprobeerd is. Een lange chat vol mislukte pogingen maakt de agent slechter.

## Valkuilen
- **Prints en foutmeldingen kunnen data bevatten.** Vraag de agent om debug-output zonder gevoelige inhoud (aantallen, kolomnamen, types). Zie [data access](data-access.md).
- De agent past de test aan zodat hij slaagt, in plaats van de code te repareren. Kijk naar wat er veranderd is.
- "Probeer het nog eens" zonder nieuwe informatie levert zelden iets op.

## Zie ook
[`grip-op-agentcode.md`](grip-op-agentcode.md) · [`data-access.md`](data-access.md) · [`workflow.md`](workflow.md) · [`../repo/testen.md`](../repo/testen.md)
