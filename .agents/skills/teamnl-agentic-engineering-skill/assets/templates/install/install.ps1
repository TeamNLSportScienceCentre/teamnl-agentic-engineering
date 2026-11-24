<#
    Installatie voor [projectnaam] op Windows.

    Sjabloon van de TeamNL-basis. Vervang de voorbeeldstap door de stappen uit
    het plan. Het script toont eerst wat er gebeurt, vraagt toestemming en voert
    daarna elke stap zichtbaar uit.

    Gebruik:
      install.cmd                 dubbelklikken (start dit script)
      install.ps1 -Overzicht      alleen tonen wat er zou gebeuren
      install.ps1 -Ja             zonder vraag uitvoeren (alleen als je de stappen kent)
#>
[CmdletBinding()]
param(
    [switch]$Overzicht,
    [switch]$Ja
)

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

# --- Stappen ------------------------------------------------------------------
# Elke stap heeft een naam, een uitleg, een controle of het onderdeel al aanwezig
# is, en een actie. Houd acties binnen de projectmap waar dat kan.
$stappen = @(
    [pscustomobject]@{
        Naam       = 'Voorbeeldstap'
        Uitleg     = 'Vervang deze stap door de echte installatiestappen uit het plan.'
        IsAanwezig = { $false }
        Actie      = { Write-Host '    (voorbeeld: er wordt niets geinstalleerd)' }
    }
    # Voorbeeld voor een Python-project; alleen gebruiken als het plan dit vraagt.
    # [pscustomobject]@{
    #     Naam       = 'Python 3.12'
    #     Uitleg     = 'Nodig om de applicatie te draaien; installatie via winget.'
    #     IsAanwezig = { [bool](Get-Command python -ErrorAction SilentlyContinue) }
    #     Actie      = { winget install --id Python.Python.3.12 --exact --accept-package-agreements --accept-source-agreements }
    # }
    # [pscustomobject]@{
    #     Naam       = 'Projectomgeving (.venv) en afhankelijkheden'
    #     Uitleg     = 'Maakt .venv in deze map en installeert requirements.txt.'
    #     IsAanwezig = { Test-Path -LiteralPath '.venv' }
    #     Actie      = {
    #         python -m venv .venv
    #         & .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    #         if ($LASTEXITCODE -ne 0) { throw 'pip install is mislukt.' }
    #     }
    # }
)

# --- Overzicht ----------------------------------------------------------------
Write-Host ''
Write-Host 'Installatie [projectnaam]' -ForegroundColor Cyan
Write-Host 'Dit gaat er gebeuren:'
$nummer = 0
foreach ($stap in $stappen) {
    $nummer++
    $status = if (& $stap.IsAanwezig) { 'al aanwezig, wordt overgeslagen' } else { 'wordt uitgevoerd' }
    Write-Host ("  {0}. {1} - {2}" -f $nummer, $stap.Naam, $status)
    Write-Host ("     {0}" -f $stap.Uitleg)
}
Write-Host ''

if ($Overzicht) {
    Write-Host 'Alleen overzicht gevraagd; er is niets gewijzigd.'
    exit 0
}

if (-not $Ja) {
    $antwoord = Read-Host 'Doorgaan? Typ j voor ja of n voor nee'
    if ($antwoord -notmatch '^(j|ja|y|yes)$') {
        Write-Host 'Afgebroken; er is niets gewijzigd.'
        exit 0
    }
}

# --- Uitvoeren ----------------------------------------------------------------
$nummer = 0
foreach ($stap in $stappen) {
    $nummer++
    Write-Host ''
    Write-Host ("[{0}/{1}] {2}" -f $nummer, $stappen.Count, $stap.Naam) -ForegroundColor Cyan
    if (& $stap.IsAanwezig) {
        Write-Host '    Al aanwezig; overgeslagen.'
        continue
    }
    try {
        & $stap.Actie
        Write-Host '    Klaar.' -ForegroundColor Green
    }
    catch {
        Write-Host ("    Mislukt: {0}" -f $_.Exception.Message) -ForegroundColor Red
        Write-Host '    Controleer of je de benodigde rechten en accounts hebt (zie README.md).'
        Write-Host '    Los dit op en start de installatie opnieuw; klaar gemelde stappen worden overgeslagen.'
        exit 1
    }
}

Write-Host ''
Write-Host 'Installatie voltooid. Zie README.md voor starten en controleren.' -ForegroundColor Green
