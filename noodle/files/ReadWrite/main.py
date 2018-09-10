#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class ReadWriter():
	'''Lesen und Schreiben in Dateien. Sensor und Aktor hauptsächlich zu Testzwecken...'''
	def __init__(self, name="ReadWriter", id=1, workspace="/tmp"):
		self.name = name
		self.id = id
		self.workspace = workspace


	def readIt( self, theFile="{}{}.tmp".format(self.name, self.id) ):
		'''Lesen von Daten'''
		with open( os.path.join(self.workspace, theFile), 'r' ) as f:
			return f.read()


	def writeIt( self, toWrite, theFile="{}{}.tmp".format(self.name, self.id) ):
		'''Schreiben von Daten'''
		with open( os.path.join(self.workspace, theFile), 'w' ) as f:
			return f.read()


# DEV-Notes:
# - Wie ist die Erreichbarkeit/Listener für diese Funktionen ?
# - Node-Klasse für dieses Noodle erforderlich