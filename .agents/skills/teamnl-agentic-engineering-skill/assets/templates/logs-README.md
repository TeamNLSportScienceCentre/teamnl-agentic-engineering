# Logs

| Map | Inhoud | In Git? |
| --- | --- | --- |
| `runtime/` | Logs van de applicatie zelf: fouten en resultaten van belangrijke verwerkingen, met tijdstip, onderdeel en status | Nee |
| `test/` | Ruwe testuitvoer, als die bewaard moet worden | Nee |

- In logs staan nooit secrets, persoonsgegevens of volledige brondata, ook niet
  in foutmeldingen.
- Bij risiconiveau hoog staan de logs van echte runs niet hier, maar in
  `LOG_DIR` buiten de repo. Een logfilter maskeert herkenbare persoonsnummers.
  Zie `.agents/skills/teamnl-agentic-engineering-skill/references/veilig-verwerken.md`.
- Bewaartermijn en beheer: [nog vast te leggen; verwijder lokale logs na controle].
- Geschoonde sessieverslagen staan niet hier, maar in `docs/handoffs/`.
- Deel logs pas met een agent of collega nadat je ze hebt opgeschoond.
