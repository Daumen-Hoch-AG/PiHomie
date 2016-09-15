#Ideensammlung SmartHouse
##Namensgebung
Irgendwas mit Py - für Python
- PyHouse
- PyHome
- SmartPyHome

##Features
- Szenen, die für x Objekte Wert x setzen
- Art Kalender, für die terminierung von Events
  * Verschiedene Eventtypen
    * Erinnerung / Notification z.B. "Rasen mähen" mit schlummern oder Sensorwert
    * Auslösen von Szenen o.ä.
- Random auslösen von Szenen für Abwesenheit / Urlaub
  * Zeiträume setzen in denen bestimmte Szenen plausibel sind
  * Zum Beispiel Jalousien nur schließen nachdem vorher das Licht im Raum eingeschaltet wurde.
- Logging von jeglichen Interaktionen und Events
- Automatische Anwesenheitserkennung durhc Bluetooth oder Wlan des Handys
##Struktur
- Zweiteilung in Engine (Logik) und Panel (Web-Panel und später APPs?)
  * DB REST API
- Connector zu verschiedenen Actoren und Sensoren
  * Tinkerforge
  * zWave
  * Philips Hue o.ä.