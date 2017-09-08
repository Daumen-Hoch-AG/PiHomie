# Initialisierung der ESP8266 Aktoren mit MicroPython

Die Initialisierung wird mit Hilfe eines USB to UART Adapters vorgenommen (3,3V). Die Pins des Aktors werden mit dem Programmer verbunden RX und TX sind hierbei über kreuz zu verbinden.


Für das beschreiben des Flash Speichers wird das Programm esptool verwendet.

	pip install esptool
    
## Löschen des Flash Speichers
Zuerst wird der Flash Speicher des ESP geleert, hierzu muss der ESP8266 im Bootloader Modus gestartet werden.

Der Device-Name (hier ttyUSB0 muss je nach Gerät angepasst werden.)

	esptool.py --port /dev/ttyUSB0 erase_flash
    
Im Anschluss den ESP vom Strom trennen und erneut im Bootloader Modus starten.

## Neue Firmware aufspielen
Die MicroPython Firmware kann unter http://micropython.org/download#esp8266 heruntergeladen werden.

Diese wird dann installiert.

	esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-vX.X.X.bin

## Aufruf der MicroPython Konsole
Vor dem notwendigen Neustart sollte das Modul über eine eigene Stromversorgung angeschlossen werden. Dann kann die Konsole aufgerufen werden, auf einem Mac und Linux geht dies mit:

	screen /dev/ttyUSB0 115200
    
Hier kann dann mit

	import webrepl_setup
    
die Remotekonsole beim Booten aktiviert werden und das Passwort gesetzt werden.

## Verbinden mit der Konsole über WLAN
Über die Webseite http://micropython.org/webrepl/ kann die Konsole aufgerufen werden und Dateien hoch- bzw. runtergeladne werden.
Nachdem die Konsole im Browser aufgerufen wurde, kann sich jetzt mit dem WLAN des Aktors verbunden werden. Es hat den Namen MicroPython-XXXXXX, das Standard-Passwort ist "micropythoN".

Die Datei boot.py wurde wie folgt angepasst, damit sich der Aktor mit dem Heim-WLAN verbindet.

    # This file is executed on every boot (including wake-boot from deepsleep)
    #import esp
    #esp.osdebug(None)
    import gc
    import webrepl

    def do_connect():
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect('<ssid>', '<password>')
            while not sta_if.isconnected():
                pass
        print('network config:', sta_if.ifconfig())

    do_connect()
    webrepl.start()
    gc.collect()
    
Nach einem Reboot sollte sich der Aktor mit dem WLAN verbunden haben und über eine per DHCP zugewiesene IP (WebREPL unter dem Standardport 8266) zu erreichen sein.
