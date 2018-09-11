#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class ReadWriter():
	'''Lesen und Schreiben in Dateien. Sensor und Aktor hauptsächlich zu Testzwecken...'''
	def __init__(self, name="ReadWriter", id=1, workspace="/tmp"):
		self.name = name
		self.id = id
		self.workspace = workspace


	def readItAll( self, theFile="{}{}.tmp".format(self.name, self.id) ):
		'''Lesen von Daten'''
		with open( os.path.join(self.workspace, theFile), 'r' ) as f:
			return f.read()


	def readItByLine( self, theFile="{}{}.tmp".format(self.name, self.id) ):
		'''Lesen von Daten'''
		result_dict = {}
		linenumber = 0
		with open( os.path.join(self.workspace, theFile), 'r' ) as f:
			for line in f:
				linenumber += 1
				result_dict[linenumber] = line
		return result_dict


	def writeItAll( self, toWrite, theFile="{}{}.tmp".format(self.name, self.id) ):
		'''Schreiben von Daten'''
		with open( os.path.join(self.workspace, theFile), 'w' ) as f:
			return f.read()


	def writeSpecificLine( self, toWrite, theLine, theFile="{}{}.tmp".format(self.name, self.id) ):
		'''Schreiben von Daten in eine bestimmte Zeile'''
		content = self.readItByLine(theFile)
		content[theLine] = toWrite
		return content

# Dieses Noodle wird wahrscheinlich über subprocess aufgerufen