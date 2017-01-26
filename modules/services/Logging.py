#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime


class Logger(object):
	"""Protokollierungsobjekt für Meldungen aller Art"""
	def __init__(self, first=False):
		# Options und Pfade (ggf. auslagern in cfg)
		logDir = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'log')
		f_status = "status.log"
		f_error = "error.log"
		f_info = "info.log"
		self.stampformat = "[%d/%b/%Y %H:%M:%S %z]"
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
		if first:
			print "Logger initialisiert. Weitere Meldungen werden folgendermaßen umgeleitet:"
			print "Status	: {}\nFehler	: {}\nInfos	: {}".format(self.STATUS, self.ERROR, self.INFO)


	def getTime(self):
		# Timestamp erstellen (Using local time !)
		#return datetime.datetime.utcnow().strftime("[%d/%b/%Y %H:%M:%S %z]")
		return datetime.datetime.now().strftime(self.stampformat)

	def calcTime(self, unixTime):
		# UNIX einlesen & Timestamp erstellen
		return datetime.datetime.fromtimestamp(unixTime).strftime(self.stampformat)


	def status(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		with open(self.STATUS, 'a') as handle:
			print >>handle, ts, text

	def error(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		with open(self.ERROR, 'a') as handle:
			print >>handle, ts, text

	def info(self, text, ts=False):
		ts = self.getTime() if not ts else self.calcTime(ts)
		with open(self.INFO, 'a') as handle:
			print >>handle, ts, text



if __name__ == "__main__":
	print "Protokollierungsmodul für Status-, Fehler- und andere Meldungen"
	print "Direct access not allowed..."
