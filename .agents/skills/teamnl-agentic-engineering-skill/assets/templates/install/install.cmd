@echo off
rem Start install.ps1. -ExecutionPolicy Bypass geldt alleen voor dit proces;
rem het beleid van de computer verandert niet.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
echo.
pause
