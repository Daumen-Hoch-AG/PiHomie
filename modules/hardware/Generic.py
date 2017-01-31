#!/usr/bin/python
# -*- coding: utf-8 -*-

class Actor(object):
	"""Schnittstellendefinition für Actoren"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.log = ServiceObject['Logger']
		self.log.status("Hello, I am the ACTOR {} and my ID is {}".format(nickname, id))

class Sensor(object):
	"""Schnittstellendefinition für Sensor"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.log = ServiceObject['Logger']
		self.log.status("Hello, I am the SENSOR {} and my ID is {}".format(nickname, id))



if __name__ == "__main__":
	print "Direct access not allowed..."