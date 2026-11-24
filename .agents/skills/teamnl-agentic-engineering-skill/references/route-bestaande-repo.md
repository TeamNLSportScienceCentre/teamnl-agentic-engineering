# Route: bestaande repository op orde brengen

Gebruik deze route in drie situaties:

- een bestaande repository moet agent-ready worden volgens de TeamNL-standaard;
- er ontbreken gerichte onderdelen;
- de TeamNL-basis moet naar een nieuwere versie.

Nieuwe functionaliteit valt buiten deze route. Bied na afronding de route Nieuwe
feature aan.

**Agent-ready** betekent dat een coding agent gericht en veilig in de repository
kan werken. Daarvoor zijn nodig:

- werkafspraken in `AGENTS.md`;
- een bruikbare README;
- afgeschermde secrets en data;
- een herkenbare structuur;
- een controle die laat zien dat het bestaande gedrag blijft werken.

## Eerst inventariseren

Lees vóór de eerste inhoudelijke vraag de toegestane projectdocumenten. Kijk ook
naar de mappenstructuur en de relevante code. Gelden er al data-afspraken? Dan
zijn die het uitgangspunt.

- **Wel lezen:** `README.md`, `AGENTS.md`, `CLAUDE.md`, `.gitignore`, manifesten
  zoals `package.json`, `requirements.txt` of `pyproject.toml`, bestaande
  plannen, beslissingen, handoffs en relevante broncode.
- **Niet openen:** data, `.env`-varianten, logs en andere mogelijk gevoelige
  bestanden. Voer geen code uit en wijzig niets.
- **Vergelijk** wat je aantreft met de kern en het geraamte in
  [standaardrepo.md](standaardrepo.md). Noteer per onderdeel of het aanwezig
  is, ontbreekt of afwijkt. De basisrepo bevat alle standaardmappen. Een
  bestaande repo krijgt alleen de mappen die het project echt nodig heeft, niet
  het hele geraamte.
- **Mogelijke secrets in de Git-geschiedenis** controleer je niet tijdens de
  intake. Die controle is een stap in het plan.

Vat de huidige staat in een paar zinnen samen in je eerste inhoudelijke vraag.
Zo kan de gebruiker corrigeren wat je verkeerd hebt begrepen.

## De zes thema's

Kort stelt hooguit één vraag per thema, Uitgebreid hooguit drie. Sla over wat
al uit de inventarisatie of het gesprek blijkt.

### 1. Doel en huidige staat

> Ik zie [korte samenvatting]. Klopt dat, en wat werkt er nog niet goed of mist er?

### 2. Aanleiding voor de update

Wat moet er op orde komen? Bijvoorbeeld:

- de repository agent-ready maken;
- een update van de TeamNL-basis;
- een gericht onderdeel, zoals de installatie, de data-afspraken, de
  TeamNL-stijl of de agentinstellingen.

> Wat wil je met deze update bereiken, en is er iets dat zeker niet mag veranderen?

### 3. Data en toegangsgrenzen

Bestaande afspraken gelden. Vraag alleen naar wat ontbreekt: wie beslist, wat
de agent mag lezen, wie de code uitvoert en welke output terug mag. Zie
[data-afspraken.md](data-afspraken.md). Leid het
[risiconiveau](data-afspraken.md#risiconiveau) af zonder extra vraag. Vergelijk
de bestaande maatregelen met wat dat niveau verplicht, en neem wat ontbreekt op
in de tabel met verschillen.

### 4. Agents en omgeving

> Met welke coding agents en op welke besturingssystemen werken jij en eventuele collega's aan dit project?

Daaruit volgen de ingangen, de instellingen en de installatieroute.

### 5. Behoud en controle

> Wat moet na de update zeker nog werken, en hoe controleren we dat nu: tests, een handmatige check of iets anders?

Is er geen controle? Stel dan een minimale automatische test of handmatige check
voor die je vóór én na de wijzigingen uitvoert.

### 6. Inrichting en Git

Werkende paden en eerdere plannen blijven behouden, tenzij een wijziging
expliciet wordt afgesproken. In Uitgebreid bespreek je hier ook de
Git-werkwijze, bijvoorbeeld één branch voor de update en één commit per stap.

## Het plan

Bewaar het plan in `docs/repo-updates/<YYYY-MM-DD-onderwerp>/plan-van-aanpak.md`.
Volgt het project een andere vaste plek voor plannen? Gebruik die. Gebruik het
sjabloon 'Repo-update' uit [plan-van-aanpak.md](plan-van-aanpak.md). Het plan
bevat:

- **Huidige staat:** wat je hebt bekeken en wat niet.
- **Verschillen met de standaard:** een tabel met per onderdeel de huidige
  situatie, het voorstel en het gevolg.
- **Behoud:** wat behouden blijft en hoe je het bestaande gedrag controleert.
- **Bouwstappen** in deze volgorde, voor zover nodig:
  1. **Secrets en data.** Scan de geschiedenis met Gitleaks. Verplaats echte
     data naar `data/private/` of naar goedgekeurde opslag. Negeren haalt
     bestaande commits niet weg. Een gevonden secret moet worden vervangen.
  2. **`.gitignore`.** Vul aan met de basis en controleer bestanden die al
     worden gevolgd, met `git ls-files` en `git check-ignore`.
  3. **Toegangsregels.** Leg in `AGENTS.md` vast wat de agent mag. Richt de
     instellingen in, met de
     [projectmap-hook](agent-inrichting.md#projectmap-hook-claude-code), en test
     ze met fictieve bestanden. Staat de projectmap-hook nog globaal bij de
     gebruiker? Stel dan voor die daar weg te halen.
  4. **`AGENTS.md` en `CLAUDE.md`.** Leg de werkafspraken vast, met
     verwijzingen naar het actieve plan, de beslissingen en de handoffs, en de
     basisversie.
  5. **`README.md`.** Beschrijf het doel, hoe je installeert, start, gebruikt en
     controleert, en welke toegang nodig is.
  6. **Structuur.** Voeg ontbrekende onderdelen toe, zoals `logs/`,
     `docs/handoffs/`, `docs/decisions.md` en `data/example/`. Verplaats
     werkende code alleen als dat nodig is. Benoem dan de gevolgen voor paden
     en imports.
  7. **Overige onderdelen.** Bijvoorbeeld de installatieroute, de TeamNL-stijl
     of de Gitleaks-controle vóór een commit.
  8. **Controle.** Bevestig dat het bestaande gedrag nog werkt.

Stel geen herindeling van werkende code voor zonder reden. Bouw pas nieuwe
functionaliteit als de update is afgerond.

## Update naar een nieuwere versie van de basis

De gebruikte basisversie staat in `AGENTS.md`, in de regel `TeamNL-basis:`.

1. **Nieuwe versie beschikbaar maken.** Vraag de gebruiker om de nieuwe versie
   van de basisrepo beschikbaar te maken als aparte map, bijvoorbeeld door die
   naast het project te clonen of als zip uit te pakken. Lees de CHANGELOG van
   de nieuwe skill.
2. **Vergelijken.** Vergelijk de bestanden van de basis met de huidige
   projectversie. Die bestanden staan in
   [standaardrepo.md](standaardrepo.md#wat-hoort-bij-de-basis-en-wat-bij-het-project).
   Toon per bestand het verschil en het gevolg voor het project.
3. **Projectafspraken behouden.** `AGENTS.md`, `README.md`, plannen,
   beslissingen en data-afspraken zijn van het project. Neem daarin alleen
   gerichte verbeteringen over, en pas na akkoord.
4. **Skillmap vervangen.** Vervang de skillmap en de ingangen per agent als
   geheel. Doe dat pas na akkoord op het plan.
5. **Vastleggen.** Werk de regel `TeamNL-basis:` in `AGENTS.md` bij. Leg de
   update vast in het plan en in een handoff.

## Na goedkeuring

Volg [uitvoeren.md](uitvoeren.md). Voer de controle op het bestaande gedrag
uit vóór de eerste wijziging en na de laatste. Een gefaalde controle stopt de
update. Meld dan wat er misging en stel herstel voor.

Plaats de coderegel uit het [watermerkje](plan-van-aanpak.md#watermerkje)
alleen als die nog niet in het project staat en de gebruiker dat wil.
