#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import ConfigParser


# Object Core #

class PiHomieObject(object):
	"""Objekt mit allen Standardmethoden, das für alle anderen Arten von Instanzen verfügbar sein soll"""
	def __init__(self):
		print "Initiere Systemservices..."
		# Core-Options
		print "-> Core-Options..."
		confFile = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'conf', 'core.conf')
		# Option händisch setzen, da erst nach der Zeile Options zur verfügung stehen
		isDEV = True
		self.opts = Options(confFile, isDEV)

		# Credential-Options
		print "-> Credentials..."
		if not self.opts.get('Paths')['creddir_abs']:
			credDir = os.path.join(os.path.dirname(os.path.realpath('__file__')), self.opts.get('Paths')['creddir_rel'])
		else:
			credDir = self.opts.get('Paths')['creddir_abs']
		cFile = self.opts.get('Paths')['credfile']
		credfile = os.path.join(credDir, cFile)
		self.cred = Options(credfile, self.opts.getBools('DEV'))

		# Database-Connector#
		#print "-> Database-Connector..."
		# - Comming Soon ! -
		
		# Logging
		print "-> Logging..."
		self.logs = Logger({'Paths':self.opts.get('Paths'), 'DEV':self.opts.getBools('DEV')})
		
		# Return
		print "Systemservices bereit !"


# SystemService Methoden (Klassen) #

class Logger(PiHomieObject):
	"""Protokollierungsobjekt für Meldungen aller Art"""
	def __init__(self, Opts):
		self.opts = Opts
		# Set logfilepaths
		if self.opts['Paths']['logdir_abs'] == "":
			logDir = os.path.join(os.path.dirname(os.path.realpath('__file__')), self.opts['Paths']['logdir_rel'])
		else:
			logDir = self.opts['Paths']['logdir_abs']
		f_status = self.opts['Paths']['logfile_status']
		f_error = self.opts['Paths']['logfile_error']
		f_info = self.opts['Paths']['logfile_info']

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
		return datetime.datetime.now().strftime(self.opts['Paths']['stampformat'])


	def calcTime(self, unixTime):
		# UNIX einlesen & Timestamp erstellen
		return datetime.datetime.fromtimestamp(unixTime).strftime(self.opts['Paths']['stampformat'])


	def status(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.opts['DEV']['dev']:
			with open(self.STATUS, 'a') as handle:
				print >>handle, "{} {}".format(ts, text)
		else:
			print "STATUS | {} {}".format(ts, text)


	def error(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.opts['DEV']['dev']:
			with open(self.ERROR, 'a') as handle:
				print >>handle, "{} {}".format(ts, text)
		else:
			print "ERROR | {} {}".format(ts, text)


	def info(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		if not self.opts['DEV']['dev']:
			with open(self.INFO, 'a') as handle:
				print >>handle, "{} {}".format(ts, text)
		else:
			print "INFO | {} {}".format(ts, text)



class Options(PiHomieObject):
	"""Protokollierungsobjekt für Meldungen aller Art"""
	def __init__(self, confPath, isDEV=False):
		try:
			checkFile = open(confPath, 'r')
		except IOError as e:
			print "Keine Berechtigung oder Datei nicht gefunden: {}".format(confPath)
			print "Einstellungen konnten nicht gelesen werden!"
			raise e
		else:
			checkFile.close()

		self.handle = ConfigParser.ConfigParser()
		self.handle.read(confPath)
		print "Einstellungen wurden gelesen aus {}".format(confPath)

		if isDEV:
			for section in self.handle.sections():
				for name, value in self.handle.items(section):
					print name, ":", value


	def get(self, abschnitt):
		values = {}
		for name, value in self.handle.items(abschnitt):
			values[name] = value
		return values

	def getBools(self, abschnitt):
		# Nicht string sondern True/False
		values = {}
		for name, value in self.handle.items(abschnitt):
			value = True if not value.lower() in ['n', 'no', 'not', 'nein', 'false', '', ' '] else False
			values[name] = value
		return values




if __name__ == "__main__":
	print "Direct access not allowed..."
