#!/usr/bin/python
# -*- coding: utf-8 -*-


class Logger(object):
	"""Protokollierungsobjekt für Meldungen aller Art"""
	def __init__(self, logDir, f_status, f_error, f_info):
		if os.access(logDir, os.W_OK):
			# Filehandler
			self.STATUS = os.path.join(logDir, f_status)
			self.ERROR = os.path.join(logDir, f_error)
			self.INFO = os.path.join(logDir, f_info)
			# Options (ggf. auslagern in cfg)
			self.stampformat = "[%d/%b/%Y %H:%M:%S %z]"
			# Return
			print "Logger initialisiert. Weitere Meldungen werden folgendermaßen umgeleitet:"
			print "Status	: {}\nFehler	: {}\nInfos	: {}".format(self.f_status, self.f_error, self.f_info)
			return True
		else:
			# Keine Schreibrechte !
			print "Keine Berechtigung zum Schreiben !"
			return False

	def getTime(self):
		# Timestamp erstellen (Using local time !)
		#return datetime.datetime.utcnow().strftime("[%d/%b/%Y %H:%M:%S %z]")
		return datetime.datetime.now().strftime(self.stampformat)

	def calcTime(self, unixTime):
		# UNIX einlesen & Timestamp erstellen
		return datetime.datetime.fromtimestamp(unixTime).strftime(self.stampformat)


	def status(self, text, ts=False):
		ts = self.getTime(self) if not ts else self.calcTime(self, ts)
		with open(self.STATUS, 'a') as handle:
			handle.write(text)

	def error(self, text, ts=False):
		ts = self.getTime(self) if not ts else self.calcTime(self, ts)
		with open(self.ERROR, 'a') as handle:
			handle.write(text)

	def info(self, text, ts=False):
		ts = self.getTime(self) if not ts else self.calcTime(self, ts)
		with open(self.INFO, 'a') as handle:
			handle.write(text)



if __name__ == "__main__":
	print "Protokollierungsmodul für Status-, Fehler- und andere Meldungen"
	print "Direct access not allowed..."
