# Lokaal secretbestand

- Wijziging: lokaal `secret.txt` aangemaakt met de opgegeven oefeninhoud. De bestaande regel `secret.txt` in `.gitignore` sluit het bestand al uit; geen extra negeerregel nodig.
- Controle: de bestandsinhoud is gecontroleerd zonder deze te loggen; `git check-ignore -v` bevestigt de negeerregel en `git ls-files` bevestigt dat het bestand niet wordt gevolgd. Git-diff gecontroleerd.
- Beperking: Node.js is niet beschikbaar, dus de automatische tests zijn niet uitgevoerd. Geen browsercontrole uitgevoerd; de app is niet gewijzigd.
- Vervolg: alleen dit geschoonde verslag committen en pushen naar `origin/main`, op verzoek van de gebruiker. Het secretbestand blijft lokaal.
