#!/usr/bin/python
# -*- coding: utf-8 -*-


class Actor(object):
	"""Allgemeiner Aktor für Rolladensteuerung"""
	def __init__(self, id, nickname, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		print "For the Log: 'Hello, I am the ACTOR {} and my ID is {}".format(nickname, id)

	def setUp(self):
		pass

	def setDown(self):
		pass

	def setPosition(self, direction, val):
		pass


class Sensor(object):
	"""Allgemeiner Sensor für Rolladensteuerung"""
	def __init__(self, id, nickname, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		print "For the Log: 'Hello, I am the SENSOR {} and my ID is {}".format(nickname, id)

	def getPosition(self):
		pass
	
	def getSystemStatus(self):
		pass



if __name__ == "__main__":
	print "Direct access not allowed..."
	#testActor = RollerShutter_Fibaro_fg222.Actor()