#!/usr/bin/python
# -*- coding: utf-8 -*-


from ..services.Logging import Logger # Relative imports nur mit from x import x


class Actor(object):
	"""Schnittstellendefinition für Actoren"""
	def __init__(self, id, nickname, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		self.log("Hello, I am the ACTOR {} and my ID is {}".format(nickname, id), "status")

	def log(self, text, mode="info", ts=False):
		if mode == "error":
			Logger().error(text, ts)
		elif mode == "status":
			Logger().status(text, ts)
		elif mode == "info":
			Logger().info(text, ts)


class Sensor(object):
	"""Schnittstellendefinition für Sensor"""
	def __init__(self, id, nickname, description=""):
		self.id = id
		self.nickname = nickname
		self.description = description
		print "For the Log: 'Hello, I am the SENSOR {} and my ID is {}".format(nickname, id)

	def log(self, text, mode="info", ts=False):
		if mode == "error":
			Logger().error(text, ts)
		elif mode == "status":
			Logger().status(text, ts)
		elif mode == "info":
			Logger().info(text, ts)



if __name__ == "__main__":
	print "Direct access not allowed..."