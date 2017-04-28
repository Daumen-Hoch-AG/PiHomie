# PiHomie - mach dich krass...

## Inhalt
- [Über das Projekt](#Projekt)
- [Funtkionsweisen](#Funktionsweise)
- [Installation](#Installation)
- [Listen:](#Listen)
  - [erforderliche Hardware (Minimalkonfiguration)](#erfHardware)
  - [untestützte Protokolle](#Protokollunterstützungen)
  - [Features](#Features)


<a name="Projekt"></a>
## Über das Projekt

Das IoT bietet viele Möglichkeiten, die von vielen verschiedenen Herstellern unterschiedlich umgesetzt werden. Hersteller von guten Heizungssteuerungen haben vielleicht keine oder nur schlecht umgesetzte Rolladensteuerungen. Eine günstige Lichtsteuerung ist nicht mehr günstig, wenn dafür ein komplettes System parallel betrieben werden muss...

**Ziel von PiHomie soll es sein mehrere Steuerungstechniken auf günstiger und weniger Hardware zu vereinen !**

Der Ansatz ist nicht neu und wurde schon mit anderen, teils sehr guten Projekten verfolgt. Trotzdem finden sind wir mit keiner der bisherigen Lösungen so richtig zufrieden und schaffen daher unsere eigene.

<a name="Funktionsweise"></a>
## Funktionsweise

PiHomie wird größtenteils mit Python umgesetzt und mit Raspberry(s) betrieben. Es soll eine REST Schnittstelle zur Ansteuerung von Sensoren und Aktoren geben.

Die Steuerung erfolgt dann über ein Webinterface auf einem festen oder mobilen Gerät, innerhalb und/oder außerhalb des Hauses. Außerdem durch Schalter im Haus und/oder am Gerät.

Obwohl ein Fokus auf sichere Übetragungen und Absicherung des Systems gelegt wird, verzichten wir auf die Ansteuerung kritischer Funktionen wie z.B. dem Haustürschloss.


<a name="Installation"></a>
## Installation
### 1. Server aufsetzen

Erforderliche Pakete:

	pip install requests bottle paste spidev

### 2. Geräte einbinden/anlernen
### 3. Grundeinstellungen


<a name="Listen"></a>
## Listen

Die Listen geben einen schnellen Überblick was unterstützt wird, was geplant ist und was man ungefähr benötigt. Für die Auflistung und die Dokumentation der einzelnen Geräte (Sensoren/Aktoren) planen wir evtl. eine GitHub-Wiki.

Der Fortschritt der geplanten Features wird bei den [Milestones in diesem Projekt](https://github.com/Daumen-Hoch-AG/PiHomie/milestones) dokumentiert.

<a name="erfHardware"></a>
### Liste erforderlicher Hardware (Minimalkonfiguration)
:white_check_mark: Raspberry Pi mit Peripherie<br>
:white_check_mark: Netzerkanbindung des Geräts (WLAN-Stick/LAN)<br>
:white_check_mark: [CUL-Stick](http://shop.busware.de/product_info.php/cPath/1/products_id/29?osCsid=ee679848ba57f850417e0814966b5014)<br>
:white_check_mark: beliebiger Sensor/Aktor (siehe Protokollunterstützung)<br>

<a name="Protokollunterstützungen"></a>
### Liste der Protokollunterstützungen
:soon: zWave (mit [RaZberry](http://razberry.z-wave.me/))<br>
:soon: 433 MHz Funk (mit [TK Remote Bricklet](https://www.tinkerforge.com/de/shop/bricklets/remote/remote-switch-bricklet.html))<br>
:soon: 433,32 MHz (mit [CUL-Stick](http://shop.busware.de/product_info.php/cPath/1/products_id/44))<br>
:soon: Homematic Funk<br>
:soon: Bluetooth<br>
:soon: IR-Steuerung<br>

<a name="Features"></a>
### Liste der Features
:soon: Weboberfläche<br>
:soon: Szenen und Kompositionen<br>
:soon: Terminierungen<br>
:soon: Abwesenheitsautomatik<br>
:soon: Information, Logging und Tarifmanagement<br>
