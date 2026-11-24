---
titel: "Branches en pull requests"
categorie: samenwerken
moeilijkheid: 2
---

# Branches en pull requests

## In één zin
Een branch is een parallelle versie van je repo om iets uit te proberen; met een pull request vraag je of die wijziging terug mag naar de hoofdversie, en kan iemand anders eerst meekijken.

## Waarom
Op `main` werken is prima zolang je alleen bent en in kleine stappen commit. Maar wil je iets groters proberen, samenwerken met een collega, of een agent iets laten bouwen dat je eerst wilt bekijken? Dan houdt een branch `main` schoon en werkend. Een pull request (PR) op GitHub laat de wijzigingen overzichtelijk zien en geeft ruimte voor review en commentaar.

## Wanneer wel, wanneer (nog) niet
- **Wel:** een grotere feature, een experiment waarvan je niet weet of het blijft, werk van een collega of een tweede agent, of wanneer iemand wil meekijken voordat het in `main` komt.
- **Nog niet:** je werkt alleen, in kleine stappen, aan een prototype. Dan voegen branches vooral stappen toe.

## Zo begin je
```bash
git switch -c grafiek-weekoverzicht        # nieuwe branch maken en erop gaan staan
# ... werken, committen zoals altijd ...
git push -u origin grafiek-weekoverzicht   # branch naar GitHub
```
Op GitHub verschijnt dan een knop **Compare & pull request**. Beschrijf wat en waarom, vraag een collega als reviewer, en klik na goedkeuring op **Merge**. Daarna lokaal:
```bash
git switch main
git pull
```
Je kunt je agent ook vragen: *"Maak een branch voor deze feature en open aan het eind een pull request met een korte beschrijving."* (met `gh`, de GitHub CLI).

In VS Code zie je de huidige branch linksonder; klik erop om te wisselen of een nieuwe te maken.

## Valkuilen
- Lang levende branches lopen uit de pas met `main` en geven merge conflicts. Houd ze kort: dagen, geen maanden.
- Vergeten op welke branch je staat. Kijk linksonder in VS Code of gebruik `git status`.
- Een pull request is geen formaliteit: lees de diff (zie [grip op agentcode](../agent/grip-op-agentcode.md)).
- Branchnamen volgen de [naamgeving](naamgeving.md): kleine letters met streepjes.

## Zie ook
[`../agent/parallel-werken.md`](../agent/parallel-werken.md) · [`../agent/issues-gedreven.md`](../agent/issues-gedreven.md) · [`../agent/builder-reviewer.md`](../agent/builder-reviewer.md) · [`werken-in-vs-code.md`](werken-in-vs-code.md)
