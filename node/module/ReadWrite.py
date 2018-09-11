#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Generic


class Sensor(Generic.Sensor):
	"""Inhalte aus einer Datei lesen (Test-Sensor)"""
	def __init__(self, id, nickname, description=""):
		super(Sensor, self).__init__(id, nickname, description="")


	def getAllValuesAsDictionary(self):
		"""Inhalt einer Dateie in einem Zeilen-Dictionary"""
		# Raise NotImplementedError
		return False

	def getMainValue(self):
		"""Gesamter Inhalt einer Datei"""
		# Raise NotImplementedError
		return False

	def getValue(self, bezeichner):
		return self.getAllValuesAsDictionary()[bezeichner]


class Actor(Generic.Actor):
	"""Inhalt in eine Datei schreiben (Test-Aktor)"""
	def __init__(self, id, nickname, description=""):
		super(Actor, self).__init__(id, nickname, description="")


	def setAll(self, wert):
		"""Inhalt in eine Datei (über-)schreiben"""
		pass

	def setParam(self, bezeichner, wert):
		"""Inhalt an eine bestimmte Stelle in einer Datei schreiben"""
		pass

	def setAllValuesAsDictionary(self, valDict):
		"""Mehrere Inhalte an mehrere Stellen einer Datei schreiben"""
		for bezeichner in valDict:
			self.setParam(bezeichner, valDict[bezeichner])


if __name__ == "__main__":
	print("Direct access not allowed...")