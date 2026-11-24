---
titel: "Parallel werken: meerdere agents, worktrees en meldingen"
categorie: hoe-werk-je-samen
moeilijkheid: 3
---

# Parallel werken: meerdere agents, worktrees en meldingen

## In één zin
Wil je meerdere agents tegelijk laten werken, geef ze dan elk een eigen kopie van je repo (een git worktree op een eigen branch), zodat ze elkaars wijzigingen niet in de weg zitten.

## Waarom
Twee agents in dezelfde map overschrijven elkaars bestanden, en je weet niet meer welke wijziging van wie is. Een worktree is een tweede werkmap van dezelfde repo, op een eigen branch. Elke agent heeft zo zijn eigen plek; jij voegt het werk daarna samen.

## Wanneer wel, wanneer (nog) niet
- **Wel:** je werkt aan twee losse dingen tegelijk (bijvoorbeeld een nieuwe grafiek én de README) en je bent vertrouwd met [branches en pull requests](../repo/branches-en-pull-requests.md).
- **Nog niet:** je bent net begonnen. Eén agent, één taak, kleine stappen is overzichtelijker dan drie halve taken. Meer tegelijk is niet sneller als je het overzicht kwijtraakt.

## Zo begin je
```bash
# vanuit je projectmap: een tweede werkmap op een nieuwe branch
git worktree add ../mijn-project-grafiek -b grafiek-weekoverzicht
```
Open `../mijn-project-grafiek` in een eigen VS Code-venster en start daar de tweede agent. Klaar? Commit en push op die branch, maak een pull request, en ruim op:
```bash
git worktree remove ../mijn-project-grafiek
```
Sommige agents (zoals de desktop-apps van Claude Code en Codex) kunnen zelf een worktree per sessie aanmaken. Kijk in de instellingen van jouw agent.

**Overzicht houden:**
- Geef elke sessie een duidelijke naam of titel, en één taak.
- Zet meldingen aan, zodat je hoort als een agent op je wacht (de meeste agents en editors hebben een instelling voor een geluid of notificatie).
- Laat elke sessie eindigen met een korte hand-off.

## Valkuilen
- Twee worktrees die hetzelfde bestand aanpassen geven later een merge conflict. Verdeel het werk op bestanden of onderdelen.
- Elke sessie kost tokens en aandacht. Drie agents die op jou wachten is geen winst.
- `.env` en `data/private/` staan niet in git en dus ook niet automatisch in een nieuwe worktree. Gebruik nepdata of kopieer bewust.

## Zie ook
[`../repo/branches-en-pull-requests.md`](../repo/branches-en-pull-requests.md) · [`workflow.md`](workflow.md) · [`builder-reviewer.md`](builder-reviewer.md)
