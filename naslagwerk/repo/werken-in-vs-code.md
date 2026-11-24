---
titel: "Praktisch in VS Code: repo openen en sessie afsluiten"
categorie: samenwerken
moeilijkheid: 1
---

# Praktisch in VS Code: repo openen en sessie afsluiten

## In één zin
Eén repo = één map = één VS Code-venster: clone hem één keer, open de map, en sluit elke werksessie af met hand-off, commit, push en venster dicht.

## Waarom
Je agent werkt in de map die je opent. Open je een bovenliggende map, dan ziet hij ook andere projecten (en hun data). Open je losse bestanden, dan mist hij `AGENTS.md`. Een vaste routine voorkomt dat je kwijtraakt waar je was.

## Wanneer wel, wanneer (nog) niet
Altijd. Dit is de dagelijkse basis.

## Zo begin je
**Eén keer: clonen**
1. Kies een vaste plek voor al je repo's, bijvoorbeeld `C:\Users\<jij>\CodeLibrary\`. Liever niet in OneDrive: synchroniseren en git gaan slecht samen.
2. VS Code: *Source Control* → **Clone Repository** → plak de GitHub-URL → kies je vaste plek. Of in de terminal: `git clone <url>`.
3. Kies **Open** (of *File → Open Folder* en kies de repomap zelf).

**Elke werksessie**
| Begin | Einde |
|---|---|
| Open de repomap (*File → Open Recent*) | Laat de agent een hand-off schrijven en lees hem |
| `git pull` (of *Sync* in Source Control) | Commit (met een duidelijk bericht) |
| Agent: *"Lees de laatste hand-off"* | Push (of *Sync*) |
| | Sluit het venster (*File → Close Folder*) |

Werk je aan twee repo's? Open ze in twee vensters (*File → New Window*), niet samen in één.

## Valkuilen
- De verkeerde map geopend: kijk bovenin de verkenner welke map open is.
- Werk dat niet gepusht is, staat alleen op jouw laptop.
- Een repo in OneDrive kan conflicterende kopieën en kapotte `.git`-mappen geven.

## Zie ook
[`../agent/workflow.md`](../agent/workflow.md) · [`../agent/waar-draait-je-agent.md`](../agent/waar-draait-je-agent.md) · [`branches-en-pull-requests.md`](branches-en-pull-requests.md) · [`handoffs-memory-decisions.md`](handoffs-memory-decisions.md)
