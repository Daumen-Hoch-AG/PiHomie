##Struktur
- Zweiteilung in Engine (Logik) und Panel (Web-Panel und später APPs?)
	* DB REST API
	* WebApp statt native App
- Connector zu verschiedenen Actoren und Sensoren
	* Tinkerforge
	* zWave
	* Philips Hue o.ä.
	* Siehe dazu: <a href="https://github.com/Daumen-Hoch-AG/SmartHouse/issues/3">Issue #3</a>
- Priorisierung der Features und Module in einer eigenen Liste
	* zur Diskussion: <a href="https://github.com/Daumen-Hoch-AG/SmartHouse/issues/2">Issue #2</a>
	* zur Prioritätenliste: <a href="https://github.com/Daumen-Hoch-AG/SmartHouse/projects/3">Project #3</a>
	
	
##Codestruktur
- Dateinamen für Sensoren und Aktoren: NameOberklasse_Hersteller_Typ.py Bsp: RollerShutter_Fibaro_fg222.py

##Programmierung
- Logging Service, auftrennen in Exception-Log und Normales-Log
	* Jede Exception führt zu einem Log-Eintrag
	* Jede Aktion z.B. Rolladen geschlossen o.ä. führt zu einem Log-Eintrag
