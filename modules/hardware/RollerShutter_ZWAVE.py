#!/usr/bin/python
# -*- coding: utf-8 -*-

import RollerShutter

#=========> Allgemeine Klassen <=================================#

# allgemeiner Aktor: zWave

class GenericActor(RollerShutter.Actor):
	"""Generic Aktor: ZWAVE RollerShutter"""
	def __init__(self, id, deviceId, instanceId, nickname, description=""):
		super(RollerShutter.Actor, self).__init__(id, nickname, description="")

	def setUp(self):
		print "Fake URI:"
		print "http://temppi:8083/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[37].Set(255)".format(self.deviceId, instanceId)
		return
	
	def setDown(self):
		print "Fake URI:"
		print "http://temppi:8083/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[37].Set(0)".format(self.deviceId, instanceId)
		return

	def setPosition(self, position):
		print "Fake URI:"
		"http://temppi:8083/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[38].Set({})".format(self.deviceId, instanceId)
		return


# allgemeiner Sensor: zWave

class GenericSensor(RollerShutter.Sensor):
	"""Generic Sensor: ZWAVE RollerShutter"""
	def __init__(self, id, nickname, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		print "For the Log: 'Hello, I am the SENSOR {} and my ID is {}".format(nickname, id)

	def getPosition(self):
		pass
	
	def getSystemStatus(self):
		pass


#=========> Spezialisierte Klassen <=============================#

# Fibaro: FGRM-222

class Fibaro_FGRM_222_Actor(GenericActor):
	"""Spezieller Aktor: Fibaro RollerShutter 2 (FG-222)"""
	def __init__(self, id, nickname, description=""):
		super(GenericActor, self).__init__(id, nickname, description="")

	def setPosition(self, position):
		print "Spezielle behandlung von up+down um das eigentlich implementierte Verhalten eines Zwave Rolladenaktors nachzuarmen (Spezialfall für den FGM222)"
		return


class Fibaro_FGRM_222_Actor(GenericSensor):
	"""Spezieller Aktor: Fibaro RollerShutter 2 (FG-222)"""
	def __init__(self, id, nickname, description=""):
		super(GenericSensor, self).__init__(id, nickname, description="")


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
