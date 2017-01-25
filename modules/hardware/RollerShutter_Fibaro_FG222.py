#!/usr/bin/python
# -*- coding: utf-8 -*-


import RollerShutter


class Actor(RollerShutter.Actor):
	"""Spezieller Aktor: Fibaro RollerShutter 2 (FG-222)"""
	def __init__(self, id, nickname, description=""):
		super(Actor, self).__init__(id, nickname, description="")

	def setUp(self):
		print "Fake URI:"
		print "http://temppi:8083/ZWave.zway/Run/devices[{}].instances[{}].commandClasses[37].Set(255)".format(3,0)
		


if __name__ == "__main__":
	print "Direct access not allowed..."



# z.B. "Küche 1"

# === Switch ===
## Down
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Set(0)
## Up
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Set(255)
## Status Update
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[37].Get()

## === Meter ===
## Update
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[38].Get()
## Set
# http://temppi:8083/ZWave.zway/Run/devices[3].instances[0].commandClasses[38].Set(78)
