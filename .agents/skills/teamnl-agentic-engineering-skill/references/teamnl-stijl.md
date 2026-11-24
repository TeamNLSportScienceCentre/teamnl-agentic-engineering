# TeamNL-stijl

Gebruik dit bij elk project met een gebruikersinterface: web, dashboard,
desktop of mobiel. Zonder interface is de stijl niet van toepassing.

## Uitgangspunten

- **Referentie.** [teamnl.org](https://www.teamnl.org/) is de visuele
  referentie. Bevestig assets en stijlafspraken aan de hand van officiële
  bestanden van NOC*NSF, voordat je ze als 'vastgesteld' presenteert.
- **Eén plek.** Logovarianten, kleurwaarden, typografie en afspraken over
  componenten staan centraal in `design.md` in de root van het project.
  `design.md` gaat voor op de standaardthema's van frameworks of andere skills.
- **Framework.** Vertaal de afspraken naar het framework van het project. Een
  webpagina gebruikt CSS-variabelen. Een desktop- of mobiele app gebruikt het
  thema- of stijlsysteem van dat framework, met dezelfde waarden.
- **Gebruiksrecht.** Gebruik geen logo, beeldmerk of foto zonder bevestigd
  gebruiksrecht. Verzin ook geen logo's, cijfers of quotes.

## Status van de huisstijlgegevens

| Onderdeel | Waarde | Status |
| --- | --- | --- |
| Lettertype | Hanken Grotesk, gewichten 300, 400, 600, 700 en 900; reserve: `sans-serif` | Waargenomen op teamnl.org op 17-11-2026. Hanken Grotesk is beschikbaar via Google Fonts (Open Font License). |
| Primair oranje | `#FF6600`, donkerder `#DD3900`, lichter `#FF9E45` | Waargenomen, niet officieel bevestigd |
| Secundair blauw | `#00378A`, donkerder `#102074`, lichter `#3976BE`, licht `#87B1E3` | Waargenomen, niet officieel bevestigd |
| Tekst | `#0F172A`, `#334155`, uitgeschakeld `#64748B` | Waargenomen |
| Achtergronden | `#FFFFFF`, `#F8FAFC`, `#F1F5F9`, `#E2E8F0`, lichtblauw `#F7F9FB` | Waargenomen |
| Signaalkleuren | fout `#EA3D3D`, succes `#69BD86` | Waargenomen |
| Logo's | Niet meegeleverd | Open punt: welke logo's mogen en willen we meeleveren? |

Er is geen openbare huisstijlgids of logokit gevonden. De
[merkenpagina van NOC*NSF](https://www.nocnsf.nl/over-nocnsf/beschermen-merken-nocstarnsf)
geeft deze regels:

- redactioneel gebruik van het logo is toegestaan;
- commercieel of promotioneel gebruik vraagt toestemming van NOC*NSF;
- de Olympische ringen en de Paralympische agitos mogen niet worden gebruikt.

De merkidentiteit kan veranderen in aanloop naar 2028. Controleer de waarden dus
opnieuw voordat een product breed wordt verspreid.

**Contrast** (berekend, controleer met een contrastchecker):

| Combinatie | Contrast | Geschikt voor |
| --- | --- | --- |
| Oranje `#FF6600` op wit | Ongeveer 2,9:1 | Alleen decoratie en grote vlakken, niet voor tekst |
| Donkere tekst `#0F172A` op oranje | Ongeveer 6:1 | Knoppen en labels |
| `#DD3900` op wit | Ongeveer 4,5:1 | Grote of vette tekst |
| Blauw `#00378A` op wit | Ongeveer 11:1 | Tekst en links |

## Hallmark gebruiken

[Hallmark](https://github.com/Nutlope/hallmark) is een design-skill (MIT) voor
onder meer Claude Code, Codex en GitHub Copilot.

- **design.md.** Hallmark leest `design.md` in de root als een vastgezet
  systeem. Dat systeem gaat voor op de eigen themacatalogus van Hallmark, en alle
  pagina's delen het.
- **Variants.** Heeft één pagina iets anders nodig? Voeg dan een sectie
  `## Variants` toe, in plaats van lokaal af te wijken.
- **Installeren.** Installeer Hallmark alleen met akkoord van de gebruiker,
  bijvoorbeeld met `npx skills add nutlope/hallmark` in de projectmap. Daarvoor
  is Node 18 of hoger nodig. Een skill van derden bevat instructies en code die
  de agent uitvoert. Lees die dus eerst, of laat de gebruiker dat doen.
- **Controleren.** Laat Hallmark een interface uitwerken of controleren met
  `audit <pad>`. De browserchecks vragen ook Chrome en `puppeteer-core`.
- **Alleen web.** Hallmark is gericht op web: HTML en CSS. Voor een desktop- of
  mobiele app gebruik je dezelfde `design.md` als bron. Je vertaalt de tokens
  dan zelf naar het framework en controleert handmatig. Werk de inzet buiten
  webinterfaces per project uit en leg die vast in het plan.

## Bij de uitvoering

1. **design.md klaarzetten.** In de basisrepo staat `design.md` al in de root.
   Kopieer anders `assets/templates/design.md` naar `design.md`. Vul de
   projectnaam in. Pas de waarden alleen aan na een
   bevestigde huisstijlbron. Vermeld die bron dan in het bestand.
2. **Tokens vertalen.** Zet de tokens om naar het framework: CSS-variabelen,
   een thema-object of een stijlbestand. Zorg dat de code de tokens gebruikt en
   geen losse kleurwaarden.
3. **Assets.** Zet geverifieerde assets in `assets/brand/`, met een README over
   de herkomst en het gebruiksrecht. Zonder bevestigd logo gebruik je een
   tekstmerk ('TeamNL' in het lettertype), geen nagemaakt logo.
4. **Controle.** Controleer contrast en leesbaarheid, en bij web ook de mobiele
   breedte. Leg de stijlkeuzes vast in `docs/decisions.md` als ze afwijken van
   `design.md`.
