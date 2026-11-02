# Korte intake: slotvraag fase 1 en plan op één A4

## Aanleiding
De intake plus het nalezen van de output duurde in de vorige sessie te lang.
De korte variant wordt de standaard voor de gezamenlijke sessies.

## Wijzigingen
- Kort houdt de bestaande vraaglimieten (één vraag per thema). Thema 6 komt in
  Kort als slotvraag na thema 8: wat moet aan het eind van de eerste
  gezamenlijke bouwsessie werken, met twee of drie voorstellen via de keuzetool.
- De output van Kort is een bouwplan voor fase 1 van maximaal één A4 (circa
  450 woorden, voetregel inbegrepen), volledig getoond in het gesprek zonder
  aparte samenvatting. Nieuw A4-sjabloon in `references/plan-van-aanpak.md`.
- Kort neemt de kern van de data-afspraken op; het volledige AGENTS.md-blok,
  de boomstructuur en `.gitignore` werkt de bouwagent bij de start uit.
- Kort staat als eerste optie en is gemarkeerd als aanbevolen. Uitgebreid is
  inhoudelijk ongewijzigd.
- Beschrijving in de drie skillbestanden, README en startcontrole bijgewerkt.
- Watermerkje minder zichtbaar: voetregel en bouwafspraak staan samen in één
  HTML-commentaar onderaan het plan, onzichtbaar in weergegeven Markdown maar
  leesbaar voor wie het ruwe bestand opent, zoals de bouwagent. De zichtbare
  regel in de startopdracht is weg. Witte tekst en witregels werken niet in
  Markdown.

## Controles
- 7 app-tests geslaagd; `git diff --check` geslaagd.
- Ankers naar thema 6, Watermerkje en agent-ready-sectie bestaan.
- Testsessie Kort + Nieuwe repository in Claude Code (VS Code), fictieve casus
  multistream-opname: twee startkeuzes, zeven themavragen en de slotvraag over
  fase 1 met drie voorstellen. Plan circa 430 woorden, binnen één A4.
  Goedgekeurd door de begeleider.

## Beperkingen
- Niet getest in Codex of Mistral Vibe, ook niet of het verborgen commentaar
  daar onzichtbaar blijft.
- In de test is de verdiepingsvraag als tekst gesteld, zodat het plan zichtbaar
  bleef; de skill schrijft daarvoor een keuzeknop voor.
- Een bouwagent kan de verborgen bouwafspraak als opvallend melden.
