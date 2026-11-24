# Data

| Map | Inhoud | In Git? |
| --- | --- | --- |
| `example/` | Fictieve of aantoonbaar deelbare voorbeelden, elk bestand < 1 MB | Ja |
| `private/` | Echte, lokale of gevoelige data, alleen binnen goedgekeurde toegang | Nee |

Ga ervan uit dat alles in `example/` openbaar wordt. Zet er dus niets gevoeligs in,
en gebruik bij voorkeur synthetische data. De agent leest `private/` niet; zie
het blok Data access in `AGENTS.md`.

## Per bestand of dataset

| Bestand | Herkomst | Fictief of echt | Gebruiksrecht | Formaat | Gevoeligheid | Toegang | Bewaartermijn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `example/[bestand]` | [gemaakt met scripts/... op basis van alleen kolomnamen] | fictief | vrij | [csv] | geen | iedereen | onbeperkt |
