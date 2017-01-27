#!/usr/bin/python
# -*- coding: utf-8 -*-


from ..services.Logging import Logger # Relative imports nur mit from x import x
import Generic


class Actor(Generic.Actor):
	"""Schnittstellendefinition für Rolladenaktoren"""
	def __init__(self, id, nickname, description=""):
		super(Generic.Actor, self).__init__(id, nickname, description="")

	def setUp(self):
		pass

	def setDown(self):
		pass

	def setPosition(self, position):
		pass


class Sensor(Generic.Sensor):
	"""Schnittstellendefinition für Rolladensensoren"""
	def __init__(self, id, nickname, description=""):
		super(Generic.Sensor, self).__init__(id, nickname, description="")

	def getPosition(self):
		pass
	
	def getSystemStatus(self):
		pass



if __name__ == "__main__":
	print "Direct access not allowed..."