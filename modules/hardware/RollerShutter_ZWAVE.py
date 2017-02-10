#!/usr/bin/python
# -*- coding: utf-8 -*-

import RollerShutter

#=========> Allgemeine Klassen <=================================#

# allgemeiner Aktor: zWave

class GenericActor(RollerShutter.Actor):
	"""Generic Aktor: ZWAVE RollerShutter"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(RollerShutter.Actor, self).__init__(id, nickname, ServiceObject, description="")
		# Diese Informationen holen:
		self.deviceId = 0 
		self.instanceId = 0
		# --------------------------

	def setParam(self, bezeichner, wert):
		if bezeichner == "isUp" or bezeichner == "isDown":
			# commandClasses 37
			print " FAKE: http://temppi:8083/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[37].Set({})".format(self.deviceId, instanceId, wert)
		else if bezeichner == "Position":
			# commandClasses 38
			print " FAKE: http://temppi:8083/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[38].Set({})".format(self.deviceId, instanceId, wert)
		else:
			self.log.error("Parameter '{}' ist so nicht änderbar")




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

#z.B. "Küche 1"

# === Switch ===
## Down
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Set(0)
## Up
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Set(255)
## Status Update
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Get()

## === Meter ===
## Update
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[38].Get()
## Set
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[38].Set(78)
