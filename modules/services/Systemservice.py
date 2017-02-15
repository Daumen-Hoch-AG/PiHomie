#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import ConfigParser



# Object Core #

class PiHomieObject(object):
	"""Objekt mit allen Standardmethoden, das für alle anderen Arten von Instanzen verfügbar sein soll"""
	def __init__(self):
		isDEV = True
		print "Initiere Systemservices..."
		self.cwd = os.path.dirname(os.path.realpath('__file__'))
		
		# Core-Options
		print "-> Core-Options..."
		confPath = os.path.join(self.cwd, 'conf', 'core.conf')
		self._checkPermissions(confPath)
		self.opts = ConfigParser.ConfigParser()
		self.opts.read(confPath)
		print "Einstellungen wurden gelesen aus {}".format(confPath)
		confPath = None

		# Credential-Options
		print "-> Credentials..."
		confPath = os.path.join(self.cwd, 'conf', 'creds.conf')
		self._checkPermissions(confPath)
		self.creds = ConfigParser.ConfigParser()
		self.creds.read(confPath)
		print "Credentials wurden gelesen aus {}".format(confPath)
		
		# Logging
		print "-> Logging..."
		self.LOGS = {
			'ERROR': os.path.join(self.cwd, 'log', 'error.log'),
			'STATUS': os.path.join(self.cwd, 'log', 'status.log'),
			'INFO': os.path.join(self.cwd, 'log', 'info.log'),
		}
		for fp in self.LOGS:
			self._checkPermissions(self.LOGS[fp], 'a')

		# Database-Connector#4
		#print "-> Database-Connector..."
		# - Comming Soon ! -
		
		# Return
		print "Systemservices bereit !"

		if isDEV:
			print "Einstellungen:"
			for section in self.opts.sections():
				for name, value in self.opts.items(section):
					print name, ":", value
			print "Credentials:"
			for section in self.creds.sections():
				for name, value in self.creds.items(section):
					print name, ":", value


	def logs(self, mode, text, ts=False):
		mode = mode.upper()
		ts = self._getTime() if not ts else self._calcTime(ts)
		if not self.opts.getboolean('DEV','dev'):
			with open(self.LOGS[mode], 'a') as handle:
				print >>handle, "{} {}".format(ts, text)
		else:
			print "{} | {} {}".format(mode, ts, text)



	# - internal helper functions

	def _getTime(self):
		# Timestamp erstellen (Using local time !)
		#return datetime.datetime.utcnow().strftime("[%d/%b/%Y %H:%M:%S %z]")
		return datetime.datetime.now().strftime(self.opts.get('Logging', 'stampformat'))

	def _calcTime(self, unixTime):
		# UNIX einlesen & Timestamp erstellen
		return datetime.datetime.fromtimestamp(unixTime).strftime(self.opts.get('Logging', 'stampformat'))

	def _checkPermissions(self, cPath, mode='r'):
		try:
			checkFile = open(cPath, mode)
		except IOError as e:
			print "Keine Berechtigung oder Datei nicht gefunden: {}".format(cPath)
			print "Einstellungen konnten nicht gelesen werden!"
			raise e
		else:
			checkFile.close()



if __name__ == "__main__":
	print "Direct access not allowed..."