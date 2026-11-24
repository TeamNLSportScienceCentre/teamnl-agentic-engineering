---
titel: "Agents en clouddataplatforms (Azure, Fabric, Databricks)"
categorie: waar
moeilijkheid: 3
---

# Agents en clouddataplatforms (Azure, Fabric, Databricks)

## In één zin
Als je editor is ingelogd op een clouddataplatform, kan je agent daar in principe ook bij: bepaal dus eerst wat hij daar mag.

## Waarom
Je agent werkt met jouw rechten. Ben je in VS Code of in de terminal ingelogd op Azure, Fabric of Databricks (bijvoorbeeld via de `az`-CLI of een extensie), dan kan een agent met terminaltoegang dezelfde opdrachten uitvoeren: data opvragen, bestanden uploaden, resources aanmaken. Dat is krachtig, maar lastig te overzien. Sommige platforms hebben ook een eigen ingebouwde AI-assistent, met eigen regels voor waar je data heen gaat.

## Wanneer wel, wanneer (nog) niet
- **Wel:** je project draait echt op zo'n platform (bijvoorbeeld IMU-bestanden in Azure, verwerking in Fabric) en je hebt een test- of ontwikkelomgeving met nep- of testdata.
- **Nog niet:** je bouwt nog op je eigen laptop. Werk dan lokaal met [nepdata](../repo/nepdata-maken.md) en koppel het platform pas als de code werkt.
- **Niet zonder overleg:** productiedata of een workspace met atleetgegevens. De data-eigenaar en IT bepalen wat mag.

## Zo begin je
1. **Scheid omgevingen:** een ontwikkel-workspace met testdata, los van productie.
2. **Minste rechten:** log voor ontwikkelwerk in met een account of rol die alleen bij die testomgeving kan, het liefst alleen lezen.
3. **Leg vast wat de agent mag** in [`AGENTS.md`](../repo/agents-md.md) en dwing het af met [permissies](permissies-en-guardrails.md) of [hooks](hooks.md), bijvoorbeeld: `az`-opdrachten altijd eerst vragen.
4. **Laat de agent code schrijven, draai hem zelf:** de agent maakt het script of notebook, jij voert het uit op het platform en geeft alleen de (opgeschoonde) uitkomst terug. Zie [data access](data-access.md).
5. **Log uit** of sluit de terminal als je klaar bent met cloudwerk.

## Valkuilen
- "Ik ben toch ingelogd" is precies het risico: inloggen geldt voor iedereen die jouw terminal gebruikt, ook je agent.
- De ingebouwde assistent van een platform valt onder de afspraken van dat platform, niet onder die van je coding agent. Vraag na wat er met je data gebeurt.
- Kosten: een agent die cloudopdrachten uitvoert kan ook resources aanmaken die geld kosten.
- Twijfel je? Vraag het je IT-afdeling of de eigenaar van het platform, niet je agent.

## Zie ook
[`waar-draait-je-agent.md`](waar-draait-je-agent.md) · [`data-access.md`](data-access.md) · [`sandbox.md`](sandbox.md) · [`hooks.md`](hooks.md)
