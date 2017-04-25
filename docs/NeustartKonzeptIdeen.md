# Kommunikation und Initialisierung Knoten
## Kommunikation zwischen Steuerung und Knoten

- Die Knoten setzen die Befehle der Steuerung auf die Kommunikationsprotokolle (z.B. WLAN, SPI, zWave) um. Hierbei wird ein Paket (Bsp: TCP/ID/Protokoll/Data) gesendet und umgesetzt.
- Der Knoten weiss zu jedem Sensor oder Aktor wie oft bzw. wann er Werte abfragen oder Senden kann. Weiterhin ordnet er die System-Id der ID des Sensors / Aktors in dem jweiligen Protokoll zu.
- Im Beispiel von zWave gewährleistet der Knoten, dass ein Kommando an den Aktor gesendet wird wenn dieser empfangsbereit ist.

## Initialisierung der Knoten

- Alle Knoten werden bei (Neu)start von der Steuerung Benachrichtigt.
- Die Nachricht enthält Informationen über die an den Knoten angeschlossenen Sensoren / Aktoren und über deren Aktualisierungs-, Abfrageintervalle und Protokolle.
- Der Knoten bestätigt wenn ein Befehl ausgeführt wurde, vorher nur "eingereiht"-Nachricht (z.B. bei zWave kann dies deutlich verzögert sein)

### Knoten Neustart

- Die Steuerung sendet in einem bestimmten Intervall eine Status-Anfrage an alle Knoten
- Ein "frischer"-Knoten antwortet mit einem "requestConfig"-Kommando und bekommt darauf hin alle initialen Daten und Konfigurationen

## Steuerkommandos an Knoten
- Während des Betriebs sind Kommandos zum Hinzufügen, Löschen und Ändern von Sensoren und Aktoren vorgesehen..