#!/usr/bin/python
# -*- coding: utf-8 -*-

class Actor(object):
	"""Schnittstellendefinition für Actoren"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.log = ServiceObject['Logger']
		self.log.status("Hello, I am the ACTOR {} and my ID is {}".format(nickname, id))

	def setParam(self, bezeichner, wert):
		self.log.error("Der Wert: {}={} konnte nicht gesetzt werden, da die Methode dafür noch nicht definiert ist.".format(bezeichner, wert))



class Sensor(object):
	"""Schnittstellendefinition für Sensor"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.log = ServiceObject['Logger']
		self.log.status("Hello, I am the SENSOR {} and my ID is {}".format(nickname, id))

	def getMainValue(self):
		self.log.error("Der Hauptwert für dieses Gerät konnte nicht zurückgegeben werden, da die Methode noch nicht definiert ist.")

	def getAllValuesAsDictionary(self):
		self.log.error("Die Werte konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.")

	def getValue(self, bezeichner):
		self.log.error("Der Wert für den Schlüssel '{}' konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.".format(bezeichner))


if __name__ == "__main__":
	print "Direct access not allowed..."
