## Überblick der API Funktionen

Der benötigte SHA1-Hash (SHA1) wird mit der Pairing-ID als Salt in Form eines Bytestrings errechnet.

Der Trenner (SEP) wird in der Konfigurationsdatei `main_config.cfg` auf dem Modul festgelegt.

Die unten gezeigten Schemata sind verkettet und ohne `+` oder ` ` zu verstehen.

### pair

Erstellen einer Verbinden zu einem bestimmten Gerät mittels IP. Sobald ein Pairing erfolgt ist, werden keine Verbindungen und Kommados eines Geräts mit einer anderen IP angenommen.

Schema:

	SHA1("pair") + SEP + IP des Pairs + SEP + ID des Moduls

### unpair

Auflösung eines Pairings. Die hinterlegten Einstellungen werden für 30 Sekunden gelöscht. In dieser Zeit muss ein Interrupt stattfinden oder der Strom getrennt werden, um ein dauerhaften Reset zu erreichen.

Schema:

	SHA1("unpair")


### roll

Relais schalten um Rolladen in eine bestimmte Richtung (R) für eine bestimmte Dauer (D) bewegen.

Schema:

	SHA1("roll") + SEP + R("up" | "down") + D(int)

### rollstatus

Den aktuellen Stand des Rolladens abfragen.

Schema:

	SHA1("rollstatus")
