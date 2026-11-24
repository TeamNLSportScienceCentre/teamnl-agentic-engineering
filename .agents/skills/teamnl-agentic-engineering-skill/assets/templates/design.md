# Design: [projectnaam]

Vastgezet stijlsysteem voor dit project, op basis van de TeamNL-stijl. Dit
bestand gaat voor op standaardthema's van frameworks en skills. Hallmark leest
het als vastgezet systeem. Bron van de waarden: waargenomen op teamnl.org op
17-11-2026, nog niet bevestigd met een officiële huisstijlbron. Vervang deze
regel door de bevestigde bron zodra die er is.

## System

- Uitstraling: helder, sportief en zakelijk. Veel wit, oranje als accent en
  blauw voor tekstaccenten en navigatie.
- Lettertype: Hanken Grotesk (Google Fonts, Open Font License) voor alle tekst.
  Gebruik gewicht 400 voor tekst, 600 voor labels en 700/900 voor koppen.
- Logo: [nog niet bevestigd]. Gebruik zonder bevestigd gebruiksrecht een
  tekstmerk 'TeamNL' in Hanken Grotesk 900. Gebruik nooit de Olympische ringen
  of Paralympische agitos.
- Contrast: oranje `#FF6600` is geen tekstkleur op wit (ongeveer 2,9:1). Gebruik op
  oranje vlakken donkere tekst `#0F172A` (ongeveer 6:1). Gebruik `#DD3900` op wit
  alleen voor grote of vette tekst (ongeveer 4,5:1).

## Tokens

```css
:root {
  --font-sans: "Hanken Grotesk", sans-serif;

  --color-primary: #ff6600;
  --color-primary-darker: #dd3900;
  --color-primary-lighter: #ff9e45;

  --color-secondary: #00378a;
  --color-secondary-darker: #102074;
  --color-secondary-lighter: #3976be;
  --color-secondary-light: #87b1e3;

  --color-text: #0f172a;
  --color-text-muted: #334155;
  --color-text-disabled: #64748b;

  --color-bg: #ffffff;
  --color-bg-subtle: #f8fafc;
  --color-bg-muted: #f1f5f9;
  --color-border: #e2e8f0;
  --color-bg-blue-light: #f7f9fb;

  --color-error: #ea3d3d;
  --color-success: #69bd86;

  --radius: 8px;
  --space: 8px;
}
```

## Controls

- Primaire knop: achtergrond `--color-primary`, tekst `--color-text`, gewicht 600.
  Bij hover: `--color-primary-darker` met witte tekst, alleen als het contrast
  is gecontroleerd. Anders donkere tekst behouden.
- Secundaire knop: rand en tekst `--color-secondary` op `--color-bg`.
- Links: `--color-secondary`, onderstreept bij hover.
- Invoervelden: rand `--color-border`, focusrand `--color-secondary`, foutmelding
  in `--color-error` met tekst (niet alleen kleur).

## Motion

- Kort en functioneel: 150–200 ms voor hover en focus, geen decoratieve animaties.
- Respecteer `prefers-reduced-motion`.

## Exports

- Web: gebruik de tokens hierboven als CSS-variabelen.
- Desktop of mobiel: vertaal dezelfde waarden naar het thema van het framework.
  Leg de plek van die vertaling hier vast: [bestand].
- Grafieken: oranje en blauw als hoofdreeksen, grijstinten voor context. Gebruik
  bij meer reeksen de lichtere varianten.
