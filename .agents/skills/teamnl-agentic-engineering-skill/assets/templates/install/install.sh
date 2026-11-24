#!/usr/bin/env bash
# Installatie voor [projectnaam] op macOS of Linux.
#
# Sjabloon van de TeamNL-basis. Vervang de voorbeeldstap door de stappen uit het
# plan. Het script toont eerst wat er gebeurt, vraagt toestemming en voert daarna
# elke stap zichtbaar uit.
#
# Gebruik:
#   bash install.sh              overzicht, vraag en uitvoeren
#   bash install.sh --overzicht  alleen tonen wat er zou gebeuren
#   bash install.sh --ja         zonder vraag uitvoeren (alleen als je de stappen kent)

set -euo pipefail
cd "$(dirname "$0")"

overzicht=0
ja=0
for arg in "$@"; do
  case "$arg" in
    --overzicht) overzicht=1 ;;
    --ja) ja=1 ;;
    *) echo "Onbekende optie: $arg" >&2; exit 2 ;;
  esac
done

# --- Stappen ------------------------------------------------------------------
# Elke stap heeft een id in STAPPEN en vier onderdelen: <id>_naam, <id>_uitleg,
# <id>_aanwezig (geeft 0 als het onderdeel er al is) en <id>_actie.
STAPPEN=(voorbeeld)

voorbeeld_naam="Voorbeeldstap"
voorbeeld_uitleg="Vervang deze stap door de echte installatiestappen uit het plan."
voorbeeld_aanwezig() { return 1; }
voorbeeld_actie() { echo "    (voorbeeld: er wordt niets geinstalleerd)"; }

# Voorbeeld voor een Python-project; alleen gebruiken als het plan dit vraagt.
# Voeg dan 'python venv' toe aan STAPPEN.
# python_naam="Python 3"
# python_uitleg="Nodig om de applicatie te draaien; installatie via Homebrew (macOS)."
# python_aanwezig() { command -v python3 >/dev/null 2>&1; }
# python_actie() { brew install python; }
#
# venv_naam="Projectomgeving (.venv) en afhankelijkheden"
# venv_uitleg="Maakt .venv in deze map en installeert requirements.txt."
# venv_aanwezig() { [ -d .venv ]; }
# venv_actie() { python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt; }

# --- Overzicht ----------------------------------------------------------------
echo
echo "Installatie [projectnaam]"
echo "Dit gaat er gebeuren:"
nummer=0
for id in "${STAPPEN[@]}"; do
  nummer=$((nummer + 1))
  naam_var="${id}_naam"
  uitleg_var="${id}_uitleg"
  if "${id}_aanwezig"; then status="al aanwezig, wordt overgeslagen"; else status="wordt uitgevoerd"; fi
  echo "  ${nummer}. ${!naam_var} - ${status}"
  echo "     ${!uitleg_var}"
done
echo

if [ "$overzicht" -eq 1 ]; then
  echo "Alleen overzicht gevraagd; er is niets gewijzigd."
  exit 0
fi

if [ "$ja" -ne 1 ]; then
  read -r -p "Doorgaan? Typ j voor ja of n voor nee: " antwoord
  case "$antwoord" in
    j|J|ja|Ja|y|Y|yes) ;;
    *) echo "Afgebroken; er is niets gewijzigd."; exit 0 ;;
  esac
fi

# --- Uitvoeren ----------------------------------------------------------------
totaal=${#STAPPEN[@]}
nummer=0
for id in "${STAPPEN[@]}"; do
  nummer=$((nummer + 1))
  naam_var="${id}_naam"
  echo
  echo "[${nummer}/${totaal}] ${!naam_var}"
  if "${id}_aanwezig"; then
    echo "    Al aanwezig; overgeslagen."
    continue
  fi
  if "${id}_actie"; then
    echo "    Klaar."
  else
    echo "    Mislukt. Controleer of je de benodigde rechten en accounts hebt (zie README.md)." >&2
    echo "    Los dit op en start de installatie opnieuw; klaar gemelde stappen worden overgeslagen." >&2
    exit 1
  fi
done

echo
echo "Installatie voltooid. Zie README.md voor starten en controleren."
