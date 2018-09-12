# Quick Start

1. Anschließen des ESP am UART und starten im Boot-Modus
1. Löschen des Flash Speichers mit dem `esptool.py`
1. Trennen der Stromverbindung und Neustart im Boot-Modus
1. Installieren der Firmware `esp8266-X-vX.X.X.bin`
1. Trennen der Stromverbindung
1. Anschluss an UART und eigener Stromverbindung für einen normaler Start
1. Zugriff über den UART und installieren der `WebREPL Konsole`
1. Anpassen der `boot.py` und ggf. `main_config.cfg` im Repository
1. Normaler Neustart und verbinden über `WebREPL Konsole`
1. Alle Dateien für den `ESP8266-Aktor` dort übertragen
1. Deaktivieren der `WebREPL Konsole`

# Initialisierung der ESP8266 Aktoren mit MicroPython

Die Initialisierung wird mit Hilfe eines USB to UART Adapters vorgenommen (3,3V). Die Pins des Aktors werden mit dem Programmer verbunden RX und TX sind hierbei über kreuz zu verbinden.


Für das beschreiben des Flash Speichers wird das Programm esptool verwendet.

	pip install esptool
    
## Löschen des Flash Speichers
Zuerst wird der Flash Speicher des ESP geleert, hierzu muss der ESP8266 im Bootloader Modus gestartet werden.

Der Device-Name (hier ttyUSB0 muss je nach Gerät angepasst werden.)

	esptool.py --port /dev/ttyUSB0 erase_flash
    
Den richtigen Pfad zur `tty` findet man am schnellsten unter Linux mit `dmesg | grep tty`.

Im Anschluss den ESP vom Strom trennen und erneut im Bootloader Modus starten.

## Neue Firmware aufspielen
Die MicroPython Firmware kann unter http://micropython.org/download#esp8266 heruntergeladen werden.

Diese wird dann installiert.

	esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-vX.X.X.bin

## Aufruf der MicroPython Konsole
Vor dem notwendigen Neustart sollte das Modul über eine eigene Stromversorgung angeschlossen werden. Dann kann die Konsole aufgerufen werden, auf einem Mac und Linux geht dies mit:

	screen /dev/ttyUSB0 115200
    
Unter Windows z.B. mit dem Tool PuTTY und den hier beschriebenen Einstellungen (mit 115200 Baud): https://warpproject.org/trac/wiki/howto/USB_UART

Hier kann dann mit

	import webrepl_setup
    
die Remotekonsole beim Booten aktiviert werden und das Passwort gesetzt werden.

## Verbinden mit der Konsole über WLAN
Über die Webseite http://micropython.org/webrepl/ kann die Konsole aufgerufen werden und Dateien hoch- bzw. runtergeladne werden.
Nachdem die Konsole im Browser aufgerufen wurde, kann sich jetzt mit dem WLAN des Aktors verbunden werden. Es hat den Namen MicroPython-XXXXXX, das Standard-Passwort ist "micropythoN".

Die Datei `boot.py` muss noch wie folgt für das eigene Heimnetzwerk angepasst werden, damit sich das Gerät verbinden kann.

    sta_if.connect('<ssid>', '<password>')

Auch die restlichen Dateien in diesem Verzeichnis müssen über die Remotekonsole übertragen werden.

Nach einem Reboot sollte sich der Aktor mit dem WLAN verbunden haben und über eine per DHCP zugewiesene IP (WebREPL unter dem Standardport 8266) zu erreichen sein.

## Eigenen Accesspoint des ESP sichern
Nachdem alle Dateien übermittelt und getestet worden sind, sollte die WebREPL Konsole wieder deaktiviert werden. Dazu einfach wieder

	screen /dev/ttyUSB0 115200

aufrufen und mit `import webrepl_setup` deaktivieren.

Alternativ kann für die WebREPL Konsole auch ein sehr sicheres Passwort verwendet werden.

Eine Verbindung zum Accesspoint kann man mit dem Standar-Kennwort aber trotzdem aufbauen !
