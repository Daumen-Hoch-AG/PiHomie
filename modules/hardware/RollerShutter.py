#!/usr/bin/python
# -*- coding: utf-8 -*-

import Generic


class Actor(Generic.Actor):
	"""Schnittstellendefinition für Rolladenaktoren"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Actor, self).__init__(id, nickname, ServiceObject, description="")

	def setUp(self):
		pass

	def setDown(self):
		pass

	def setPosition(self, position):
		pass


class Sensor(Generic.Sensor):
	"""Schnittstellendefinition für Rolladensensoren"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Sensor, self).__init__(id, nickname, ServiceObject, description="")

	def getPosition(self):
		pass
	
	def getSystemStatus(self):
		pass



if __name__ == "__main__":
	print "Direct access not allowed..."