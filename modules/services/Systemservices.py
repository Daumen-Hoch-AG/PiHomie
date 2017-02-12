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
		if self.Options.get('Paths','logDir_abs') == "":
			logDir = os.path.join(os.path.dirname(os.path.realpath('__file__')), self.Options.get('Paths','logDir_rel'))
		else:
			logDir = self.Options.get('Paths','logDir_abs')
		f_status = self.Options.get('Paths', 'logFileStatus')
		f_error = self.Options.get('Paths', 'logFileError')
		f_info = self.Options.get('Paths', 'logFileInfo')

		# Filehandler
		self.STATUS = os.path.join(logDir, f_status)
		self.ERROR = os.path.join(logDir, f_error)
		self.INFO = os.path.join(logDir, f_info)
		# Check Permissions
		for fp in [self.STATUS, self.ERROR, self.INFO]:
			try:
				checkFile = open(fp, 'a')
			except IOError as e:
				print "Keine Berechtigung bei: {}".format(fp)
				print "Logger wurde nicht initialisiert !"
				return
			else:
				checkFile.close()

		# Startmessage
		print "Logger initialisiert. Weitere Meldungen werden folgendermaßen umgeleitet:"
		print "Status	: {}\nFehler	: {}\nInfos	: {}".format(self.STATUS, self.ERROR, self.INFO)



	def getTime(self):
		# Timestamp erstellen (Using local time !)
		#return datetime.datetime.utcnow().strftime("[%d/%b/%Y %H:%M:%S %z]")
		return datetime.datetime.now().strftime(self.Options.get('Paths', 'stampformat'))


	def calcTime(self, unixTime):
		# UNIX einlesen & Timestamp erstellen
		return datetime.datetime.fromtimestamp(unixTime).strftime(self.Options.get('Paths', 'stampformat'))


	def status(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.Options.getboolean('DEV', 'dev'):
			with open(self.STATUS, 'a') as handle:
				print >>handle, "{} {}".format(ts, text)
		else:
			print "STATUS | {} {}".format(ts, text)


	def error(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.Options.getboolean('DEV', 'dev'):
			with open(self.ERROR, 'a') as handle:
				print >>handle, "{} {}".format(ts, text)
		else:
			print "ERROR | {} {}".format(ts, text)


	def info(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.Options.getboolean('DEV', 'dev'):
			with open(self.INFO, 'a') as handle:
				print >>handle, "{} {}".format(ts, text)
		else:
			print "INFO | {} {}".format(ts, text)


class Credentials(object):
	"""Protokollierungsobjekt für Meldungen aller Art"""
	def __init__(self, ServiceObject, Parser):
		# Read systemconfig
		self.Options = ServiceObject['Opt']
		self.log = ServiceObject['Logger']
		self.creds = {}

		# Set credfilepaths
		if self.Options.get('Paths','credDir_abs') == "":
			credDir = os.path.join(os.path.dirname(os.path.realpath('__file__')), self.Options.get('Paths','credDir_rel'))
		else:
			credDir = self.Options.get('Paths','credDir_abs')

		# Creds aus File lesen
		cFile = self.Options.get('Paths', 'credFile')
		cFile = os.path.join(credDir, cFile)
		try:
			checkFile = open(cFile, 'r')
		except IOError as e:
			self.log.error("Keine Berechtigung oder Datei nicht gefunden: {}".format(cFile))
			self.log.error("Credentials wurde nicht gelesen !")
			return
		else:
			checkFile.close()

		self.credConfig = Parser.ConfigParser()
		self.credConfig.read(cFile)

	def getCred(self, abschnitt):
		creds = {}
		for name, value in self.credConfig.items(abschnitt):
			creds[name] = value
		return creds

		self.log.info("Credentials wurden gelesen aus {}".format(cFile))




if __name__ == "__main__":
	print "Direct access not allowed..."
