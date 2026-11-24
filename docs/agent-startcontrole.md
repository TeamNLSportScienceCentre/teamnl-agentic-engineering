# Agents starten en controleren

Start de agent vanuit de map van je eigen project, met de twee skillmappen erin
(zie de README). De commando's met $ of / hieronder typ je in het gesprek met de
agent, niet in PowerShell of een andere shell.

| Agent | Terminal | In het agentgesprek | Skilllocatie |
| --- | --- | --- | --- |
| Codex | codex | $teamnl-agentic-engineering-skill | .agents/skills/teamnl-agentic-engineering-skill/SKILL.md |
| Claude Code | claude | /teamnl-agentic-engineering-skill | .claude/skills/teamnl-agentic-engineering-skill/SKILL.md |
| GitHub Copilot | chat in agentmodus, of copilot | /teamnl-agentic-engineering-skill | .agents/skills/teamnl-agentic-engineering-skill/SKILL.md |
| Mistral Vibe Code | vibe | /teamnl-agentic-engineering-skill | .agents/skills/teamnl-agentic-engineering-skill/SKILL.md |

Op Windows kun je codex.cmd en claude.cmd gebruiken als PowerShell de .ps1-
starters blokkeert. Verander daarvoor geen systeembeleid. Mistral Vibe laadt
projectskills alleen uit vertrouwde projectmappen; controleer de inhoud voordat
je de map in Vibe als vertrouwd markeert. Deze uitleg gaat over Vibe Code,
niet over het importeren van skills in Vibe Work.

De Claude-map bevat een eigen SKILL.md als ingang en verwijst naar dezelfde
centrale instructies als Codex en Vibe. Zo zijn er geen drie inhoudelijke kopieën
die uiteen kunnen lopen. Herstart de agentsessie na het hernoemen van een skill.

## Handmatige acceptatie per agent

Gebruik een oefenmap met de twee skillmappen en een fictieve casus, zonder echte
data. De scenario's met het verwachte gedrag staan in
[acceptatietests.md](../.agents/skills/teamnl-agentic-engineering-skill/acceptatietests.md).
Begin met deze:

1. **Scenario 1.** Een oefenmap zonder eigen bestanden: de eerste reactie vat
   samen wat de skill ziet en vraagt in één beurt naar de route, de variant en
   de suggestiemodus, met knoppen als die er zijn en anders als tekst.
2. **Scenario 2.** Nieuw project, Kort, een dashboard voor een verzonnen
   sportteam: één vraag per beurt, het plan past op één A4 en staat volledig in
   het gesprek. Vóór goedkeuring verandert er niets behalve het plan.
3. **Scenario 19.** Een oefenmap met een fictieve notitie, een script en een
   databestand: de skill noemt het databestand alleen als soort, vraagt eerst
   waarvoor de bestanden zijn en zet ze met een rol en een plek in het plan.

## Uitgevoerde controle op 16 oktober 2026 (intake-skill 1.x)

- Claude Code 2.1.197: claude.cmd --version en --help uitgevoerd.
- Codex CLI 0.144.4: codex.cmd --version en --help uitgevoerd.
- Gewone PowerShell-starters werden door execution policy geblokkeerd; .cmd werkt.
- Mistral Vibe: niet geïnstalleerd/in PATH; geen lokale uitvoering mogelijk.
- Skillpaden, lokale Markdown-links en naamgeving worden statisch gecontroleerd.
- Volledige interactieve intake en zichtbaarheid in de drie agents nog niet
  uitgevoerd. Versie/help controleren bewijst niet dat de intake correct draait.
- Voorbeelden in het bredere naslagwerk voor installaties, pushes, containers,
  externe diensten en agents zijn geen uitgevoerde tests. Voer alleen toepasselijke
  voorbeelden uit op een oefenrepo met de benodigde accounts.

## Officiële documentatie

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Mistral Vibe Code skills](https://docs.mistral.ai/vibe/code/cli/skills)
- [Claude Code permissions](https://code.claude.com/docs/en/permissions)
