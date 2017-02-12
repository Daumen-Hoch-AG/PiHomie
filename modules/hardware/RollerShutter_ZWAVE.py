#!/usr/bin/python
# -*- coding: utf-8 -*-

import RollerShutter
from requests import post
from requests.auth import HTTPBasicAuth

#=========> Allgemeine Klassen <=================================#

# allgemeiner Aktor: zWave

class GenericActor(RollerShutter.Actor):
	"""Generic Aktor: ZWAVE RollerShutter"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(RollerShutter.Actor, self).__init__(id, nickname, ServiceObject, description="")
		self.creds = ServiceObject['Creds'].getCred('Zwave')
		# Diese Informationen asu DB holen:
		self.deviceId = 3
		self.instanceId = 0
		# --------------------------

	def setParam(self, bezeichner, wert):
		if bezeichner == "isUp" and wert:
			# -- commandClasses 37
			url = 'http://{}/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[37].Set(255)'.format(self.creds['url'], self.deviceId, self.instanceId)
		elif bezeichner == "isDown" and wert:
			# -- commandClasses 37
			url = 'http://{}/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[37].Set(0)'.format(self.creds['url'], self.deviceId, self.instanceId)
		elif bezeichner == "Position":
			# -- commandClasses 38
			url = 'http://{}/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[37].Set({})'.format(self.creds['url'], self.deviceId, self.instanceId, wert)
		else:
			self.log.error("Parameter '{}' ist so nicht änderbar".format(bezeichner))
			return False
		# Execute
		result = post(url, auth=HTTPBasicAuth(self.creds['username'], self.creds['password']))
		if result.status_code == 200:
			self.log.status("Wert {}={} für Device {} (Instance {}) gesetzt.".format(bezeichner, wert, self.deviceId, self.instanceId))
			return True
		else:
			self.log.error("Fehler beim setzen des Werts {}={} für Device {} (Instance {}) - Die Anfrage gab den Code {} zurück!".format(bezeichner, wert, self.deviceId, self.instanceId, result.status_code))
			return False

#	Ggf. ist bei Zwave eine Methode besser, der in einem Request meherere Werte setzt...
#	def setAllValuesAsDictionary(self, valDict):
#		pass



# allgemeiner Sensor: zWave

class GenericSensor(RollerShutter.Sensor):
	"""Generic Sensor: ZWAVE RollerShutter"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.log.status("For the Log: 'Hello, I am the SENSOR {} and my ID is {}".format(nickname, id))


	#(( NON STANDARD FUNCTIONS ))#

	def getPosition(self):
		pass



#=========> Spezialisierte Klassen <=============================#

# Fibaro: FGRM-222

class Fibaro_FGRM_222_Actor(GenericActor):
	"""Spezieller Aktor: Fibaro RollerShutter 2 (FG-222)"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(GenericActor, self).__init__(id, nickname, ServiceObject, description="")

	#def setPosition(self, position):
		# Berechnung der notwendigen Motorlaufzeit um ca. auf die angegebene Position zu fahren


class Fibaro_FGRM_222_Actor(GenericSensor):
	"""Spezieller Aktor: Fibaro RollerShutter 2 (FG-222)"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(GenericSensor, self).__init__(id, nickname, ServiceObject, description="")


# ? anderer Hersteller: Modell ?


if __name__ == "__main__":
	print "Direct access not allowed..."

#=========> Notizen <================================================#

# ZWave Device API (direkter Zugriff ins ZWAVE Netz)
#
# Für jede Funktionsweise eines Gerätes wird eine eigene Instanz angelegt mit fortlaufender ID.
# Gibt es nur eine Instanz ist die ID=0 und die Angabe davon kann weggelassen werden.
# Alle Variablen/Commands einer Instanz befinden sich dann in den verscheidenen 'commandClasses'.
# Management Funktionen sind davon losgelöst im Objekt 'controller' oder dem Toplevel 'z-way'.
#
# Für jedes Command entweder Credentials übermitteln oder ein Cookie bekommen.
# 1. : curl -v -g -u USER:PW http://....
#
# Daten: http://yourip:8083/ZWaveAPI/Data/*
# Setten: http://yourip:8083/ZWaveAPI/Run/devices[x].instances[y].commandClasses[z].*
#
# z.B. "Küche 1"
# === Switch ===
## Up & Down
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Set(255)
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Set(0)

## Status Update
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Get()

## === Meter ===
## Update
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[38].Get()
## Set
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[38].Set(78)
