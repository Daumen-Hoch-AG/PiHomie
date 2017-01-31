#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime


# core classes

class Logger(object):
	"""Protokollierungsobjekt für Meldungen aller Art"""
	def __init__(self, ServiceObject):
		# Read systemconfig
		self.Options = ServiceObject['Opt']

		# Set logfilepaths
		if self.Options.get('Logging','logDir_abs') == "":
			logDir = os.path.join(os.path.dirname(os.path.realpath('__file__')), self.Options.get('Logging','logDir_rel'))
		else:
			logDir = self.Options.get('Logging','logDir_abs')
		f_status = self.Options.get('Logging', 'logFileStatus')
		f_error = self.Options.get('Logging', 'logFileError')
		f_info = self.Options.get('Logging', 'logFileInfo')

		# Filehandler
		self.STATUS = os.path.join(logDir, f_status)
		self.ERROR = os.path.join(logDir, f_error)
		self.INFO = os.path.join(logDir, f_info)
		# Check Permissions
		for fp in [self.STATUS, self.ERROR, self.INFO]:
			try:
				checkFile = open(fp)
			except IOError as e:
				print "Keine Berechtigung bei: {}".format(fp)
				raise ########### <<<<<<<<< Exception RAISE !
			else:
				checkFile.close()

		# Startmessage
		print "Logger initialisiert. Weitere Meldungen werden folgendermaßen umgeleitet:"
		print "Status	: {}\nFehler	: {}\nInfos	: {}".format(self.STATUS, self.ERROR, self.INFO)



	def getTime(self):
		# Timestamp erstellen (Using local time !)
		#return datetime.datetime.utcnow().strftime("[%d/%b/%Y %H:%M:%S %z]")
		return datetime.datetime.now().strftime(self.Options.get('Logging', 'stampformat'))


	def calcTime(self, unixTime):
		# UNIX einlesen & Timestamp erstellen
		return datetime.datetime.fromtimestamp(unixTime).strftime(self.Options.get('Logging', 'stampformat'))


	def status(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.Options.getboolean('DEV', 'dev'):
			with open(self.STATUS, 'a') as handle:
				print >>handle, ts, text
		else:
			print "STATUS |", ts, text


	def error(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.Options.getboolean('DEV', 'dev'):
			with open(self.ERROR, 'a') as handle:
				print >>handle, ts, text
		else:
			print "ERROR |", ts, text


	def info(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.Options.getboolean('DEV', 'dev'):
			with open(self.INFO, 'a') as handle:
				print >>handle, ts, text
		else:
			print "INFO| ", ts, text


if __name__ == "__main__":
	print "Direct access not allowed..."
