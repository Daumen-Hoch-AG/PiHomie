# Grobkonzept der REST API (BottlePy)
## Verwaltungsfunktionen
### Etagen
- Alle Etagen zurückgeben
- Alle Räume einer Etage zurückgeben
- Hinzufügen
- Ändern
- Löschen

### Räume
- Alle Räume zurückgeben `http://server:port/rooms`
- Hinzufügen `http://server:port/rooms/add`(Übergabe per Post oder Parameter?)
- Ändern `http://server:port/rooms/edit`
- Löschen `http://server:port/rooms/delete`

### Sensoren + Aktoren
- Alle Sensoren/Aktoren liefern `http://server:port/sensors`
- Alle Sensoren/Aktoren eines Raums liefern `http://server:port/sensors/<room>`
- Hinzufügen 
- Ändern
- Löschen

### Szenen
- Szene hinzufügen
- Szene ändern
- Szene löschen
- Szene auslösen

### Szenen-Gruppen
- Gruppe hinzufügen
- Szene einer Gruppe hinzufügen
- Szene aus einer Gruppe entfernen
- Gruppe Löschen
- Gruppe auslösen

## Betriebsfunktionen
### Sensoren
- letzten Sensorwert lesen
- Sensorwerte aus Zeitraum (Timestamp bis Timestamp) lesen

### Aktoren
- Zustand (aktuellen Wert) des Aktors lesen
- validen Wertebereich eines Aktors lesen
- Wert eines Aktors setzen




