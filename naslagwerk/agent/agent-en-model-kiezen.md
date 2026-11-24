---
titel: "Welke agent, welk model, hoeveel denkwerk?"
categorie: waar
moeilijkheid: 2
---

# Welke agent, welk model, hoeveel denkwerk?

## In één zin
Claude Code, Codex en Copilot lijken meer op elkaar dan je denkt: kies op basis van wat je organisatie toestaat en wat voor jou werkt, en stel per taak in hoe zwaar het model mag nadenken.

## Waarom
"Welke is de beste?" verandert elke paar maanden. Wat blijft: de werkwijze (plan, kleine stappen, hand-offs, `AGENTS.md`) werkt met elke agent. En met de instelling voor *effort* of *reasoning* kies je tussen snel en goedkoop, of grondig en duurder.

## Wanneer wel, wanneer (nog) niet
Kies één agent en word daar handig in. Wissel pas als je tegen een concrete grens aanloopt (licentie, functie, kwaliteit bij jouw soort taak).

## Zo begin je

**Agent kiezen**
| Vraag | Waarom |
|---|---|
| Welk account of welke licentie heb je via je werk? | Bepaalt ook wat er met je data gebeurt (gratis accounts trainen vaak op je data) |
| Waar wil je werken: VS Code, terminal, desktop-app? | Zie [waar draait je agent?](waar-draait-je-agent.md) |
| Leest hij `AGENTS.md`? | Dan neem je je afspraken mee als je wisselt |

**Model en effort**
- **Snel / laag:** kleine, duidelijke taken: een tekst aanpassen, een bestand hernoemen, een simpele vraag.
- **Hoog:** een plan maken, een lastige fout vinden, iets ontwerpen dat je later niet makkelijk verandert, code reviewen.
- Hoger kost meer tijd en tokens. Begin standaard en zet hem omhoog als de agent het niet goed doet of als de taak belangrijk is.
- Waar de instelling zit verschilt per agent en versie (bijvoorbeeld een modelkeuze of een effort-instelling in de chat of in de configuratie). Controleer de documentatie van jouw agent.

## Valkuilen
- Een sterker model maakt een vaag verzoek niet duidelijker. Een goede opdracht helpt meer, zie [prompten](prompten.md).
- Twee agents door elkaar in één project zonder gedeelde afspraken geeft verwarring. Zet afspraken in `AGENTS.md`, niet in de chat.
- Vergelijk niet op één poging: dezelfde vraag geeft soms een ander antwoord.

## Zie ook
[`waar-draait-je-agent.md`](waar-draait-je-agent.md) · [`config-levels.md`](config-levels.md) · [`prompten.md`](prompten.md) · [`../repo/agents-md.md`](../repo/agents-md.md)
