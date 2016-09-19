#Ideensammlung SmartHouse
##Namensgebung
Irgendwas mit Py - für Python
- PyHouse
- PyHome
- MyPyHome
- SmartPyHome
- SmartPy
- Shawn (**S**mart**H**ome-System with **A**utomated and **W**ireless **N**etwork)


##Features
- Szenen, die für x Objekte Wert x setzen
- Art Kalender, für die Terminierung von Events
	* Verschiedene Eventtypen
		* Erinnerung / Notification z.B. "Rasen mähen" mit schlummern oder Sensorwert
		* Auslösen von Szenen o.ä.
		* Vorhersehen von Ereignissen (Heizung im Bad bereits vor dem Aufstehen anschalten)
- Random auslösen von Szenen für Abwesenheit / Urlaub
	* Zeiträume setzen in denen bestimmte Szenen plausibel sind
	* Zum Beispiel Jalousien nur schließen nachdem vorher das Licht im Raum eingeschaltet wurde.
- Logging von jeglichen Interaktionen und Events
- Automatische Anwesenheitserkennung durch Bluetooth oder Wlan des Handys

##Struktur
- Zweiteilung in Engine (Logik) und Panel (Web-Panel und später APPs?)
	* DB REST API
	* WebApp statt native App
- Connector zu verschiedenen Actoren und Sensoren
	* Tinkerforge
	* zWave
	* Philips Hue o.ä.
- Priorisierung der Features in einer eigenen Liste