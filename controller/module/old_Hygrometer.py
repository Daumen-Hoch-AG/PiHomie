#!/usr/bin/python
# -*- coding: utf-8 -*-

import Generic


class Sensor(Generic.Sensor):
	"""Schnittstellendefinition für Temperatur und Feuchtigkeit"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Sensor, self).__init__(id, nickname, ServiceObject, description="")


	def getAllValuesAsDictionary(self):
		return {'Temperatur':[0, "°C"], 'Feuchte':[0, "% rel."]}

	def getMainValue(self):
		"""Feuchte in relativen Prozent zur Temperatur"""
		val = self.getAllValuesAsDictionary()['Feuchte']
		return val

	def getValue(self, bezeichner):
		return self.getAllValuesAsDictionary()[bezeichner]



if __name__ == "__main__":
	print "Direct access not allowed..."