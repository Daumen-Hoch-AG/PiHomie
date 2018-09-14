#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import current_app


class Noodle(object):
	"""Allgemeine Noodle Definition"""

	def __init__(self, options, data, callback):
		self.id = options.get('id', False)
		self.callback = callback
		self.LOG = {
			'info': current_app.logger.info,
			'warning': current_app.logger.warning,
			'error': current_app.logger.error,
		}
		self.LOG['info']( "Hello ! {} mit ID {} wurde initialisiert".format( self.getTypeId(), self.id) )

	@classmethod
	def getTypeId(cls):
		return cls.__name__


class Actor(Noodle):
	"""Schnittstellendefinition für Actoren"""
	def __init__(self, options, data, callback):
		super().__init__(options, data, callback)

	def setValue(self, options, data):
		pass

	def setValuesAsDictionary(self, options, data):
		pass
	
	def alert(self, data, options):
		pass

	def configure(self):
		pass


class Sensor(Noodle):
	"""Schnittstellendefinition für Sensor"""
	def __init__(self, options, data, callback):
		super().__init__(options, data, callback)


	def getMainValue(self, options):
		pass

	def getValuesAsDictionary(self, options):
		pass

	def getValue(self, options):
		pass

	def alert(self, data, options):
		pass

	def configure(self, options):
		pass
	
	@classmethod
	def getTypeId(cls):
		return cls.__name__


if __name__ == "__main__":
	print("Direct access not allowed...")
