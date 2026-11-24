# Installatie: volledig, met zichtbare toestemming

De installatie regelt alles wat nodig is om het programma te gebruiken, ook
ontbrekende basisprogramma's. Daarbij gelden drie afspraken:

- **Vooraf** ziet de gebruiker wat er wordt geïnstalleerd of gewijzigd, en geeft
  daarvoor toestemming.
- **Tijdens** de uitvoering blijft zichtbaar wat er gebeurt.
- **Bij een probleem** ziet de gebruiker wat die zelf moet regelen, zoals rechten
  of accounts.

## Route per besturingssysteem

Maak een route voor de besturingssystemen die de gebruikers echt gebruiken. Die
staan in het plan. De exacte scripts en runtimes volgen uit het project.

| Systeem | Bestanden | Starten |
| --- | --- | --- |
| Windows | `install.ps1` met `install.cmd` als starter | Dubbelklik op `install.cmd` |
| macOS of Linux | `install.sh` | `bash install.sh` in Terminal |

De sjablonen staan in `assets/templates/install/`. Zet de scripts in de root van
het project, of in `scripts/` met een duidelijke verwijzing in de README. Elk
script:

1. **Toont een overzicht.** Per stap staat erin wat er gebeurt, waarom dat nodig
   is en of het onderdeel al aanwezig is.
2. **Vraagt toestemming.** De gebruiker antwoordt met `j` of `n`. Met
   `-Overzicht` (Windows) of `--overzicht` (macOS en Linux) toont het script
   alleen het overzicht.
3. **Voert zichtbaar uit.** Elke stap toont een kop en het resultaat. Bij een
   fout stopt het script met een begrijpelijke melding.
4. **Werkt waar mogelijk alleen in de projectmap.** Een projectomgeving, zoals
   `.venv` bij Python, staat in de projectmap. Een basisprogramma installeert het
   script via de gangbare pakketbeheerder: `winget` op Windows, Homebrew op
   macOS en de pakketbeheerder van de distributie op Linux. Het script noemt
   dat vooraf.

Het script wijzigt geen systeembeleid. `install.cmd` start PowerShell met
`-ExecutionPolicy Bypass`. Dat geldt alleen voor dat ene proces en verandert de
instelling van de computer niet. Is een installatie met beheerdersrechten
nodig? Meld dat vooraf, en vraag de rechten niet stilzwijgend aan.

## Afhankelijkheden

- Leg de afhankelijkheden reproduceerbaar vast, met de belangrijke versies
  vastgezet. Voorbeelden zijn `requirements.txt` of `pyproject.toml` met
  lockfile bij Python, en `package.json` met lockfile bij JavaScript.
- Gebruik een aparte projectomgeving waar dat past, zoals een venv bij Python.
  Installeer niets globaal als het lokaal kan.
- Ontwikkelhulpmiddelen staan los van wat de eindgebruiker nodig heeft. Een
  voorbeeld is `pre-commit` voor de Gitleaks-controle. Zet ze in een aparte
  sectie van de README, of achter een optie in het script.

## README en grenzen van de installatie

De README beschrijft:

- de startinstructie per besturingssysteem;
- wat het script installeert;
- hoe je controleert of het gelukt is;
- wat de gebruiker zelf moet regelen.

Bij hardware, cloudplatforms en mobiele apps vermeldt de README ook wat een
script niet kan vervangen. Denk aan accounts, toegang, apparatuur, certificaten,
ontwikkelaarsprogramma's of externe voorwaarden. Bied waar mogelijk een
demonstratie aan met fictieve gegevens in `data/example/`, zodat iemand het
programma kan proberen zonder toegang tot echte data.

## Testen

Test de route op de besturingssystemen uit het plan, bij voorkeur op een schone
omgeving. Controleer drie dingen:

1. het overzicht met de optie voor alleen het overzicht;
2. het afbreken bij `n`;
3. een volledige installatie.

Leg in de handoff vast op welke systemen is getest en wat niet is getest.
