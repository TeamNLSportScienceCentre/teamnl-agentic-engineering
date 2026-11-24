---
titel: "Grip op wat je agent maakt"
categorie: grip
moeilijkheid: 1
---

# Grip op wat je agent maakt

## In één zin
Je hoeft niet elke regel te lezen, maar je moet wel weten wát er veranderd is, waaróm, en hoe je controleert dat het klopt.

## Waarom
Een agent schrijft in een paar minuten meer code dan jij op een dag leest. Als je niets meer terugleest, weet je na een week niet meer wat er in je project staat. Dat voelt onoverzichtelijk en soms spannend, en terecht: jij bent verantwoordelijk voor wat je deelt.

## Wanneer wel, wanneer (nog) niet
Altijd. Hoe dieper je kijkt, hangt af van het risico: een tijdelijk plotje vraagt minder controle dan een berekening die een coach gebruikt.

## Zo begin je
1. **Kleine stappen:** één feature per keer, één commit per werkende stap. Kleine diffs kun je wel lezen.
2. **Kijk naar de diff,** niet naar het hele bestand: in VS Code via *Source Control*, of met `git diff`. Groen is erbij, rood is eraf.
3. **Laat het uitleggen:** *"Vat in 5 regels samen wat je hebt veranderd en waarom. Welke bestanden, welke functies?"* en *"Wat is het risico van deze wijziging?"*
4. **Laat het bewijzen:** *"Hoe kan ik zelf controleren dat dit klopt?"* Draai het, en laat waar het kan een [test](../repo/testen.md) maken.
5. **Houd de structuur bij:** laat de agent de README en de mappenstructuur bijwerken als er iets bij komt. Kun jij je repo in twee minuten aan een collega uitleggen?
6. **Tweede paar ogen:** laat een aparte sessie of een collega reviewen, zie [builder / reviewer](builder-reviewer.md).

## Valkuilen
- "Het werkt" is niet hetzelfde als "het klopt". Een grafiek kan er goed uitzien met een verkeerde eenheid.
- Grote wijzigingen in één keer ("bouw het hele dashboard") zijn niet meer te controleren. Knip ze op.
- Code die je niet begrijpt en ook niet getest hebt, deel je niet met een coach.

## Zie ook
[`workflow.md`](workflow.md) · [`builder-reviewer.md`](builder-reviewer.md) · [`../repo/testen.md`](../repo/testen.md) · [`debuggen.md`](debuggen.md)
