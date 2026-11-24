---
titel: "Begrippenlijst"
categorie: overzicht
moeilijkheid: 1
---

# Begrippenlijst

## In één zin
De begrippen uit de sessies op één plek, kort uitgelegd en met een verwijzing naar het onderwerp in dit naslagwerk.

## Waarom
"Soms blijft het abracadabra, al die termen." Deze lijst helpt je de woorden te herkennen. Je hoeft ze niet uit je hoofd te kennen: zoek ze op, of vraag je agent ze uit te leggen met deze lijst erbij.

## Wanneer wel, wanneer (nog) niet
Altijd bij de hand. Ook als printversie in het overzicht (pdf).

## Zo begin je

**Agent en model**
| Begrip | Betekenis |
|---|---|
| Agent / coding agent | Een taalmodel dat zelf bestanden mag lezen en schrijven en commando's mag uitvoeren ([waar draait je agent](agent/waar-draait-je-agent.md)) |
| Model | Het taalmodel achter de agent (bijv. Claude, GPT) ([agent en model kiezen](agent/agent-en-model-kiezen.md)) |
| Prompt | Jouw opdracht of vraag aan de agent ([prompten](agent/prompten.md)) |
| Context | Alles wat de agent tijdens een gesprek weet: prompt, bestanden, `AGENTS.md` |
| Tokens | De "woorden" waarin een model rekent; meer tokens = duurder en trager |
| Planmodus | De agent mag alleen lezen en een plan voorstellen, nog niets veranderen |
| Effort | Hoe grondig het model nadenkt; hoger is beter maar trager en duurder |
| Permissies | Wat de agent zelf mag, eerst moet vragen of nooit mag ([permissies](agent/permissies-en-guardrails.md)) |
| Hook | Automatische controle vóór een actie van de agent die hem kan tegenhouden ([hooks](agent/hooks.md)) |
| Sandbox | Een afgeschermde omgeving waarin de agent alleen bij het nodige kan ([sandbox](agent/sandbox.md)) |
| Skill | Herbruikbaar instructiebestand (`SKILL.md`) voor een terugkerende taak ([skills](repo/skills.md)) |
| MCP | Een standaard om extra tools aan je agent te koppelen ([tools en MCP](agent/tools-en-mcp.md)) |
| Hand-off | Overdrachtsnotitie: waar zijn we gebleven, wat is de volgende stap? |
| Diff | De wijzigingen tussen twee versies: groen erbij, rood eraf |

**Git en GitHub**
| Begrip | Betekenis |
|---|---|
| Repository (repo) | Een projectmap die git bijhoudt, met de hele geschiedenis |
| Git / GitHub | Git houdt versies bij op je computer; GitHub bewaart ze online en deelt ze |
| Clone | Een kopie van een repo van GitHub naar je computer halen |
| Commit | Een bewust gebundelde set wijzigingen met een bericht dat zegt waarom |
| Push / fetch / pull | Commits naar GitHub sturen / kijken wat er nieuw is / het nieuwe ophalen en samenvoegen |
| Merge conflict | Twee wijzigingen op dezelfde regel: jij kiest |
| Branch | Een parallelle versie van je repo ([branches](repo/branches-en-pull-requests.md)) |
| Pull request (PR) | Een verzoek om een branch terug te voegen, met ruimte voor review |
| Worktree | Een tweede werkmap van dezelfde repo, op een eigen branch ([parallel werken](agent/parallel-werken.md)) |
| Issue | Een taak of probleem op GitHub ([issues](agent/issues-gedreven.md)) |

**Bestanden in je repo**
| Begrip | Betekenis |
|---|---|
| `README.md` | Uitleg voor mensen: wat doet het, hoe start je het? |
| `AGENTS.md` / `CLAUDE.md` | Werkafspraken voor je agent |
| `plan-van-aanpak.md` | Doel, aanpak, data en structuur (uit de intake-skill) |
| `.gitignore` | Wat git moet negeren, zoals `.env` en `data/private/` |
| `.env` / `.env.example` | Lokale instellingen en geheimen / het voorbeeld zonder echte waarden |
| `.venv` / `requirements.txt` | Eigen Python-omgeving (niet in git) / lijst met benodigde packages |
| `data/example/` / `data/private/` | Nepdata (wel in git) / echte data (niet in git) |
| Nepdata | Verzonnen voorbeelddata ([nepdata maken](repo/nepdata-maken.md)) |
| Test | Code die automatisch controleert of je project nog klopt ([testen](repo/testen.md)) |
| MVP | Minimum viable product: de kleinste versie die een echte gebruiker helpt |

## Valkuilen
- Een begrip herkennen is niet hetzelfde als het nodig hebben. Gebruik de [moeilijkheid](README.md) om te kiezen.
- Mis je een begrip? Vraag je agent: *"Leg uit wat X betekent, met een voorbeeld uit mijn project."*

## Zie ook
[`README.md`](README.md) · [`agent/workflow.md`](agent/workflow.md) · [`repo/folder-structure.md`](repo/folder-structure.md)
