---
titel: "Minder toestemmingsvragen, zonder risico"
categorie: wat-mag-hij
moeilijkheid: 1
---

# Minder toestemmingsvragen, zonder risico

## In één zin
Sta veilige, steeds terugkerende acties vooraf toe, zodat je alleen nog nadenkt over de acties die ertoe doen.

## Waarom
Als je elke 15 seconden op "toestaan" moet klikken, ga je óf stoppen, óf blind klikken. Allebei slecht. Wie alles goedkeurt zonder te lezen, heeft geen controle meer; wie afhaakt, heeft niets aan de agent.

## Wanneer wel, wanneer (nog) niet
- **Wel:** acties die niets kapotmaken en je vaak goedkeurt: `git status`, `git diff`, tests draaien, bestanden in je projectmap lezen.
- **Niet:** pushen, installeren, verwijderen, alles wat buiten je projectmap komt of je logins gebruikt (mail, OneDrive, Azure, je browser).
- **Alles toestaan** alleen in een [sandbox](sandbox.md) zonder je echte data en logins.

## Zo begin je
1. Werk een dag zoals je gewend bent en noteer wat je steeds goedkeurt.
2. Zet die acties in de projectinstellingen als *allow*, zie het voorbeeld in [permissies en guardrails](permissies-en-guardrails.md). Gebruik "altijd toestaan voor dit project" in de agent zelf als die optie er is; dan komt de regel in je instellingen terecht en kun je hem teruglezen.
3. Laat risicovolle acties op *ask* staan en verboden acties op *deny*.

**Klikt de agent in een programma (bijvoorbeeld Power BI)?** Dan vraagt hij per klik toestemming, en dat blijft traag. Kijk of het via bestanden of een script kan: laat de agent bijvoorbeeld de berekeningen, queries of exportbestanden maken die jij daarna opent. Bestanden kun je ook in git volgen; klikken niet.

## Valkuilen
- Een te brede regel (`Bash(*)` of "alles in deze map") is hetzelfde als alles toestaan.
- *Allow*-regels gelden per project of voor al je projecten, afhankelijk van waar ze staan. Zie [configuratie: user level vs. project level](config-levels.md).
- Minder vragen betekent niet minder controleren: kijk nog steeds naar de diff vóór je commit.

## Zie ook
[`permissies-en-guardrails.md`](permissies-en-guardrails.md) · [`hooks.md`](hooks.md) · [`config-levels.md`](config-levels.md) · [`sandbox.md`](sandbox.md)
