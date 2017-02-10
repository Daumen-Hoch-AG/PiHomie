#!/usr/bin/python
# -*- coding: utf-8 -*-

import Generic


class Sensor(Generic.Sensor):
	"""Schnittstellendefinition für Temperatur und Feuchtigkeit"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Sensor, self).__init__(id, nickname, ServiceObject, description="")

	def getMainValue(self):
		"""Temperatur in Grad Celsius"""
		pass

	def getAllValuesAsDictionary(self):
		pass

	def getValue(self, bezeichner):
		pass



if __name__ == "__main__":
	print "Direct access not allowed..."