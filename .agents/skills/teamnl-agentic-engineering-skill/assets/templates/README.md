# [projectnaam]

[Eén of twee zinnen: wat doet dit project en voor wie.]

## Wat heb je nodig

- [Besturingssysteem of -systemen waarop het werkt.]
- [Accounts, toegang of apparatuur die je zelf moet regelen, en bij wie.]
- [Data: waar echte data vandaan komt en hoe je toegang krijgt. Echte data staat niet in Git.]

## Installeren

**Windows:** dubbelklik op `install.cmd`.
**macOS of Linux:** open Terminal in deze map en typ `bash install.sh`.

Het script laat eerst zien wat er wordt geïnstalleerd of gewijzigd en vraagt dan
om toestemming. Met `install.cmd -Overzicht` of `bash install.sh --overzicht`
zie je alleen het overzicht. [Wat de installatie niet kan regelen, zoals een
account of apparatuur.]

## Starten

```text
[exact startcommando]
```

## Gebruiken

[Korte uitleg van de belangrijkste handeling. Zonder echte data kun je het
proberen met de fictieve voorbeelden in `data/example/`.]

## Controleren

- Automatische tests: `[exact testcommando]`.
- Handmatige controle: [wat je ziet als het werkt].

## Voor ontwikkelaars

- Werkafspraken voor coding agents: `AGENTS.md`. Plannen: `docs/project/` en `specs/`.
- Beslissingen: `docs/decisions.md`. Sessieverslagen: `docs/handoffs/`.
- Controle op secrets vóór elke commit, eenmalig per computer:
  `pip install pre-commit` en daarna `pre-commit install`.
- Kopieer `.env.example` naar `.env` en vul je eigen waarden in, als het project
  configuratie nodig heeft. Deel `.env` nooit.
- Gemaakt met de TeamNL-standaardrepo; de versie staat in `AGENTS.md`.
