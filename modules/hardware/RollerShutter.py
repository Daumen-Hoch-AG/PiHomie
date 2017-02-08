#!/usr/bin/python
# -*- coding: utf-8 -*-

import Generic


class Actor(Generic.Actor):
	"""Schnittstellendefinition für Rolladenaktoren"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Actor, self).__init__(id, nickname, ServiceObject, description="")

	def setParam(self, bezeichner, wert):
		pass


class Sensor(Generic.Sensor):
	"""Schnittstellendefinition für Rolladensensoren"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Sensor, self).__init__(id, nickname, ServiceObject, description="")

	def getMainValue(self):
		"""Position des Rolladens"""
		pass

	def getAllValuesAsDictionary(self):
		pass

	def getValue(self, bezeichner):
		pass



if __name__ == "__main__":
	print "Direct access not allowed..."