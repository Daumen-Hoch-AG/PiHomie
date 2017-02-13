#!/usr/bin/python
# -*- coding: utf-8 -*-

class Actor(object):
	"""Schnittstellendefinition für Actoren"""
	def __init__(self, id, nickname, SysSrv, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.SYS = SysSrv
		self.SYS.logs.status("Hello, I am the ACTOR {} and my ID is {}".format(nickname, id))

	def setParam(self, bezeichner, wert):
		self.SYS.logs.error("Der Wert: {}={} konnte nicht gesetzt werden, da die Methode dafür noch nicht definiert ist.".format(bezeichner, wert))

	def setAllValuesAsDictionary(self, valDict):
		self.SYS.logs.error("Es konnten keine Werte gesetzt werden, da die Methode dafür noch nicht definiert ist. Werte: {}".format(valDict))


class Sensor(object):
	"""Schnittstellendefinition für Sensor"""
	def __init__(self, id, nickname, SysSrv, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.SYS = SysSrv
		self.SYS.logs.status("Hello, I am the SENSOR {} and my ID is {}".format(nickname, id))

	def getMainValue(self):
		self.SYS.logs.error("Der Hauptwert für dieses Gerät konnte nicht zurückgegeben werden, da die Methode noch nicht definiert ist.")

	def getAllValuesAsDictionary(self):
		self.SYS.logs.error("Die Werte konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.")

	def getValue(self, bezeichner):
		self.SYS.logs.error("Der Wert für den Schlüssel '{}' konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.".format(bezeichner))


if __name__ == "__main__":
	print "Direct access not allowed..."
