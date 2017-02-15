#!/usr/bin/python
# -*- coding: utf-8 -*-

import Generic


class Actor(Generic.Actor):
	"""Schnittstellendefinition für Rolladenaktoren"""
	def __init__(self, id, nickname, description=""):
		super(Actor, self).__init__(id, nickname, description="")


	def setParam(self, bezeichner, wert):
		pass

	def setAllValuesAsDictionary(self, valDict):
		for bezeichner in valDict:
			self.setParam(bezeichner, valDict[bezeichner])



class Sensor(Generic.Sensor):
	"""Schnittstellendefinition für Rolladensensoren"""
	def __init__(self, id, nickname, description=""):
		super(Sensor, self).__init__(id, nickname, description="")


	def getAllValuesAsDictionary(self):
		return {
			'id':self.id,
			'Position':[0, "% geschlossen"],
			"isDown":False, "isUp":False,
			"rollingSeconds":0.0
			}

	def getMainValue(self):
		"""Position des Rolladens"""
		val = self.getAllValuesAsDictionary()['Position']
		return val

	def getValue(self, bezeichner):
		return self.getAllValuesAsDictionary()[bezeichner]



if __name__ == "__main__":
	print "Direct access not allowed..."