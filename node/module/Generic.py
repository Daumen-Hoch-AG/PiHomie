#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Actor(object):
	"""Schnittstellendefinition für Actoren"""
	def __init__(self, id, nickname, description=""):
		#self.HOMIE = PIHOMIE
		self.id = id
		self.nickname = nickname
		self.description = description
		#self.HOMIE.logs('STATUS', "Hello, I am the ACTOR {} and my ID is {}".format(nickname, id))

	def setParam(self, bezeichner, wert):
		#self.HOMIE.logs('ERROR', "Der Wert: {}={} konnte nicht gesetzt werden, da die Methode dafür noch nicht definiert ist.".format(bezeichner, wert))
		pass
	
	def setAll(self, wert):
		pass

	def setAllValuesAsDictionary(self, valDict):
		#self.HOMIE.logs('ERROR', "Es konnten keine Werte gesetzt werden, da die Methode dafür noch nicht definiert ist. Werte: {}".format(valDict))
		pass


class Sensor(object):
	"""Schnittstellendefinition für Sensor"""
	def __init__(self, id, nickname, description=""):
		#self.HOMIE = PIHOMIE
		self.id = id
		self.nickname = nickname
		self.description = description
		#self.HOMIE.logs('STATUS', "Hello, I am the SENSOR {} and my ID is {}".format(nickname, id))

	def getMainValue(self):
		#self.HOMIE.logs('ERROR', "Der Hauptwert für dieses Gerät konnte nicht zurückgegeben werden, da die Methode noch nicht definiert ist.")
		pass

	def getAllValuesAsDictionary(self):
		#self.HOMIE.logs('ERROR', "Die Werte konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.")
		pass

	def getValue(self, bezeichner):
		#self.HOMIE.logs('ERROR', "Der Wert für den Schlüssel '{}' konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.".format(bezeichner))
		pass


if __name__ == "__main__":
	print("Direct access not allowed...")
