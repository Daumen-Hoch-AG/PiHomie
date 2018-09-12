#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Actor(object):
	"""Schnittstellendefinition für Actoren"""
	def __init__(self, options, data, callback):
		self.id = options.get(id, False)
		self.callback = callback
		#self.HOMIE.logs('STATUS', "Hello, I am the ACTOR {} and my ID is {}".format(nickname, id))
	
	def setValue(self, options, data):
		pass

	def setValuesAsDictionary(self, options, data):
		#self.HOMIE.logs('ERROR', "Es konnten keine Werte gesetzt werden, da die Methode dafür noch nicht definiert ist. Werte: {}".format(valDict))
		pass
	
	def alert(self, data, options):
		pass

	def configure(self):
		pass
	
	@classmethod
	def getTypeId(cls):
		return cls.__name__


class Sensor(object):
	"""Schnittstellendefinition für Sensor"""
	def __init__(self, options, data, callback):
		self.id = options.get(id, False)
		self.callback = callback
		#self.HOMIE.logs('STATUS', "Hello, I am the SENSOR {} and my ID is {}".format(nickname, id))

	def getMainValue(self, options):
		#self.HOMIE.logs('ERROR', "Der Hauptwert für dieses Gerät konnte nicht zurückgegeben werden, da die Methode noch nicht definiert ist.")
		pass

	def getValuesAsDictionary(self, options):
		#self.HOMIE.logs('ERROR', "Die Werte konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.")
		pass

	def getValue(self, options):
		#self.HOMIE.logs('ERROR', "Der Wert für den Schlüssel '{}' konnte nicht zurückgegeben werden, da die Methode dafür noch nicht definiert ist.".format(bezeichner))
		pass

	def alert(self, data, options):
		pass

	def configure(self, options):
		pass
	
	@classmethod
	def getTypeId(cls):
		return cls.__name__


if __name__ == "__main__":
	print("Direct access not allowed...")
