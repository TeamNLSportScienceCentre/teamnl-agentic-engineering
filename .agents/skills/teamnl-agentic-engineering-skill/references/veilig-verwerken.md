# Veilig verwerken van gevoelige data

Leesblokkades en hooks bepalen wat de agent mag openen. Ze houden niet tegen wat
de code zelf naar buiten brengt. Een script kan een paspoortnummer naar het
scherm printen, in een log zetten, in een tijdelijk bestand schrijven of in een
foutmelding tonen. Bij risiconiveau gevoelig en hoog bouwt de agent daarom de
maatregelen hieronder in de code zelf. Hij doet dat in de eerste bouwstappen die
met data werken. Het risiconiveau staat in
[data-afspraken.md](data-afspraken.md#risiconiveau).

| Maatregel | Gevoelig | Hoog |
| --- | --- | --- |
| 1. Paden via configuratie | Aanbevolen | Verplicht, met de echte-data-sleutel en een controle bij het starten |
| 2. Alleen samenvattingen tonen | Verplicht | Verplicht |
| 3. Foutmeldingen zonder waarden | Verplicht | Verplicht |
| 4. Logfilter | Aanbevolen | Verplicht |
| 5. Lektest | Aanbevolen | Verplicht |

De voorbeelden zijn in Python. Werk je in een andere taal? Bouw dan dezelfde
maatregelen. Vooral de lektest werkt in elke taal: draai het programma op nepdata
en zoek de nepwaarden terug in alles wat het heeft gemaakt.

## 1. Paden via configuratie

- De code leest de mappen uit `.env`, met `DATA_DIR`, `OUTPUT_DIR` en `LOG_DIR`.
  Er staat nergens een vast pad naar echte data in de code.
- Zonder instelling wijzen de mappen naar fictieve data in de repo. Draait de
  agent de code zonder `.env`, dan raakt die alleen voorbeelddata.
- **Echte-data-sleutel (bij hoog).** De code gebruikt de echte mappen alleen als
  `TEAMNL_ECHTE_DATA=1` is gezet. Zonder sleutel valt de code terug op de
  fictieve data. Ook als een agent het programma per ongeluk start, raakt het
  dan geen echte data.
  - **Waar je de sleutel zet.** Alleen in je eigen terminal, vlak voor je het
    programma start. Nooit in `.env`; staat hij daar, dan stopt de code.
  - **Geen agent in die terminal.** Start in die terminal geen agent. De
    beschermhook weigert shellcommando's waarin de sleutel staat, en ook alle
    shellcommando's als de sleutel in de omgeving van de agent staat.
- Bij hoog controleert de code bij het starten dat een ingestelde map buiten de
  repo ligt. Ligt die erbinnen, dan stopt de code met een melding zonder pad.

```python
import os
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]  # pas aan aan de plek van dit bestand
SLEUTEL = "TEAMNL_ECHTE_DATA"


def map_uit_config(naam: str, standaard: str) -> Path:
    """Geeft de echte map uit .env, maar alleen met de echte-data-sleutel. Anders de fictieve map."""
    if os.environ.get(SLEUTEL) != "1":
        return REPO / standaard
    env_bestand = REPO / ".env"
    if env_bestand.exists() and re.search(rf"^\s*(export\s+)?{SLEUTEL}\s*=", env_bestand.read_text(encoding="utf-8"), re.M):
        raise SystemExit(f"{SLEUTEL} staat in .env. Zet de sleutel alleen in je eigen terminal.")
    waarde = os.environ.get(naam)
    if not waarde:
        raise SystemExit(f"{naam} ontbreekt in .env.")
    pad = Path(waarde).expanduser().resolve()
    if pad == REPO or REPO in pad.parents:
        raise SystemExit(f"{naam} wijst naar een map in de repository. Bij risiconiveau hoog moet die erbuiten liggen.")
    return pad
```

Lees `.env` in met bijvoorbeeld `python-dotenv`, en roep `map_uit_config`
daarna aan, bijvoorbeeld als `map_uit_config("DATA_DIR", "data/example")`. Zo
start je het programma met echte data:

| Systeem | Commando, in je eigen terminal |
| --- | --- |
| macOS of Linux | `TEAMNL_ECHTE_DATA=1 python -m mijn_project` |
| Windows PowerShell | `$env:TEAMNL_ECHTE_DATA = "1"; python -m mijn_project; Remove-Item Env:TEAMNL_ECHTE_DATA` |

## 2. Alleen samenvattingen tonen

- **Wel:** aantallen, kolomnamen, statussen, rij- en kolomnummers en de duur.
- **Niet:**
  - waarden of hele rijen, ook niet een paar rijen als voorbeeld;
  - bestandsnamen waarin namen kunnen staan, zoals `paspoort-jansen.jpg`.

  Toon in plaats daarvan het aantal bestanden.
- **Geen debug-prints van records.** Gebruik de logger. Die gaat door het
  logfilter, een losse `print` niet.

## 3. Foutmeldingen zonder waarden

- Vang fouten per record af. Meld het rijnummer, de kolom en de soort fout.
- Bibliotheken zetten de waarde vaak zelf in hun foutmelding. `int()` meldt
  bijvoorbeeld welke tekst het niet kon omzetten. Log daarom het type van de
  fout, niet de tekst ervan.
- Vang op het hoogste niveau alle fouten af. Log het type en het onderdeel waar
  het misging, en stop met een foutcode.

```python
try:
    sessie_duur = int(rij["duur_min"])
except ValueError as fout:
    logger.warning("Rij %d, kolom %s: %s", rijnummer, "duur_min", type(fout).__name__)
```

## 4. Logfilter

Het filter maskeert herkenbare persoonsnummers in elke logregel, ook in de
foutdetails. Koppel het aan elke handler, ook aan die naar het scherm. Een
filter op de logger zelf geldt niet voor meldingen van onderliggende loggers.

```python
import logging
import re
from pathlib import Path

# Gelijk aan PATRONEN in .agents/hooks/bescherm-gevoelige-data.py en aan .gitleaks.toml.
PATRONEN = [
    re.compile(r"\b[A-NP-Z]{2}[A-NP-Z0-9]{6}[0-9]\b"),  # paspoort- of ID-kaartnummer (NL)
    re.compile(r"\b[0-9]{9}\b"),  # negen cijfers: mogelijk een BSN
    re.compile(r"\b[PI][A-Z<][A-Z]{3}[A-Z0-9<]{25,}"),  # eerste MRZ-regel van een reisdocument
    re.compile(r"[A-Z0-9<]{9}[0-9][A-Z<]{3}[0-9]{6}[0-9][MFX<][0-9]{6}[0-9]"),  # tweede MRZ-regel
]


def maskeer(tekst: str) -> str:
    for patroon in PATRONEN:
        tekst = patroon.sub("[GEMASKEERD]", tekst)
    return tekst


class MaskeerFilter(logging.Filter):
    """Maskeert herkenbare persoonsnummers in de melding en in de foutdetails."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.msg, record.args = maskeer(record.getMessage()), None
        if record.exc_info and not record.exc_text:
            record.exc_text = logging.Formatter().formatException(record.exc_info)
        if record.exc_text:
            record.exc_text = maskeer(record.exc_text)
        if record.stack_info:
            record.stack_info = maskeer(record.stack_info)
        return True


def stel_logging_in(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    handlers = [logging.FileHandler(log_dir / "app.log", encoding="utf-8"), logging.StreamHandler()]
    for handler in handlers:
        handler.addFilter(MaskeerFilter())
    logging.basicConfig(level=logging.INFO, handlers=handlers,
                        format="%(asctime)s %(levelname)s %(name)s %(message)s")
```

Het filter is een vangnet. Het herkent alleen vaste formaten, en geen namen,
geboortedata of foto's. Maatregel 2 en 3 blijven dus de eerste bescherming.

## 5. Lektest

De lektest draait het hele proces op nepdata met herkenbare nepwaarden. Daarna
controleert hij dat die waarden nergens terechtkomen:

- in de schermuitvoer;
- in de logs;
- in uitvoerbestanden;
- in tijdelijke bestanden.

Zet ook een foute regel in de nepdata, zodat de foutafhandeling meedoet. Bouw de
nepwaarden in delen op, zodat de Gitleaks-regels voor persoonsnummers het
testbestand niet melden.

```python
# tests/test_geen_lek.py
from mijn_project.verwerk import main  # vervang door de hoofdfunctie van het project

NEP_PASPOORT = "XX" + "1234567"
NEP_BSN = "9999" + "99990"
NEP_NAAM = "Kanarie" + "Testpersoon"


def test_geen_waarden_in_uitvoer_logs_of_bestanden(tmp_path, monkeypatch, capsys):
    data = tmp_path / "data"
    data.mkdir()
    (data / "invoer.csv").write_text(
        "naam,paspoortnummer,bsn,duur_min\n"
        f"{NEP_NAAM},{NEP_PASPOORT},{NEP_BSN},60\n"
        f"{NEP_NAAM},{NEP_PASPOORT},{NEP_BSN},onbekend\n",  # foute regel: test ook de foutafhandeling
        encoding="utf-8",
    )
    monkeypatch.setenv("TEAMNL_ECHTE_DATA", "1")  # de echte route, maar met nepdata buiten de repo
    monkeypatch.setenv("DATA_DIR", str(data))
    monkeypatch.setenv("OUTPUT_DIR", str(tmp_path / "output"))
    monkeypatch.setenv("LOG_DIR", str(tmp_path / "logs"))

    main()

    scherm = capsys.readouterr()
    teksten = [scherm.out, scherm.err]
    for bestand in tmp_path.rglob("*"):
        if bestand.is_file() and data not in bestand.parents:
            teksten.append(bestand.read_text(encoding="utf-8", errors="ignore"))
    for nep in (NEP_PASPOORT, NEP_BSN, NEP_NAAM):
        assert not any(nep in tekst for tekst in teksten), "nepwaarde gelekt naar uitvoer, logs of bestanden"
```

Moet een uitvoerbestand juist wel waarden bevatten, bijvoorbeeld een rapport
voor de coach? Sla dat bestand dan over in de lektest. Controleer in plaats
daarvan dat `OUTPUT_DIR` bij hoog buiten de repo ligt. De agent leest zo'n
rapport nooit.

De lektest draait mee met de gewone tests. Faalt hij, dan is dat een blokkade:
herstel eerst het lek.
