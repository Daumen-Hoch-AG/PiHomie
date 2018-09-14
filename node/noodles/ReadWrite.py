#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .Generic import Sensor, Actor
import os


class Reader(Sensor):
	"""Inhalte aus einer Datei lesen (Test-Sensor)"""

	def __init__(self, options, data, callback):
		super().__init__(options, data, callback)
		self.workspace = data.get('workspace', "/tmp")
		self.file = data.get('file', "ReadWriter"+str(self.id)+".tmp")
		self.path = os.path.join(self.workspace, self.file)


	def getValuesAsDictionary(self, options):
		"""Inhalt der Dateie in einem Zeilen-Dictionary"""
		result_dict = {}
		linenumber = 0
		mode = options.get('mode', 'all')
		startLine = options.get('start', False)
		endLine = options.get('end', False)
		with open( self.path, 'r' ) as f:
			for line in f:
				linenumber += 1
				lineKey = str(linenumber)
				if mode == 'range':
					if lineKey >= startLine and lineKey <= endLine:
						result_dict[lineKey] = line
				elif mode == 'one':
					if lineKey == startLine:
						result_dict[lineKey] = line
				else:
					result_dict[lineKey] = line
		return result_dict, 200


	def getMainValue(self, options):
		"""Gesamter Inhalt der Datei"""
		with open( self.path, 'r' ) as f:
			result = f.read()
		return {'result':result}, 200


	def getValue(self, options):
		"""Inhalt einer Zeile"""
		bezeichner = options.get('bezeichner', False)
		if not bezeichner:
			raise KeyError("Methode benötigt eine Option 'bezeichner' die die Zeilennummer angibt!")
		return self.getValuesAsDictionary( {'mode': 'one', 'start': bezeichner} )


	def alert(self, data, options):
		"""Methode für proaktive Rückmeldung bei Änderung in der Datei"""
		#TODO: Polling und Callback implementieren
		#self.callback()
		pass



class Writer(Actor):
	"""Inhalt in eine Datei schreiben (Test-Aktor)"""

	def __init__(self, options, data, callback):
		super().__init__(options, data, callback)
		self.workspace = data.get('workspace', "/tmp")
		self.file = data.get('file', "ReadWriter"+str(self.id)+".tmp")
		self.path = os.path.join(self.workspace, self.file)


	def setAll(self, options, data):
		"""Inhalt in eine Datei (über-)schreiben"""
		payload = data.get('payload', False)
		if not payload:
			raise KeyError("Methode benötigt Daten 'payload' für den Dateiinhalt!")
		else:
			with open(self.path, 'w') as f:
				f.write(payload)
				return {}, 200


	def setValue(self, options, data):
		"""Inhalt an eine bestimmte Stelle in einer Datei schreiben"""
		return self.setValuesAsDictionary(options, data)


	def setValuesAsDictionary(self, options, data):
		"""Mehrere Inhalte an mehrere Stellen einer Datei schreiben"""
		oldContent = dict()
		if os.path.exists(self.path):
			lineNumber = 0
			# Read
			with open(self.path, 'r') as f:
				for line in f:
					lineNumber += 1
					lineKey = str(lineNumber)
					oldContent[lineKey] = line
			# Merge
			data = {**oldContent, **data}

		# Write
		with open(self.path, 'w') as f:
			max_data = int( max(data, key=int) )
			max_old = int( max(oldContent, key=int) )
			lastLine = max_data if max_data > max_old else max_old
			for i in range(1, lastLine+1):
				line = str(i)
				if line in data:
					f.write(data[line])
				else:
					f.write("\n")

		return {}, 200



if __name__ == "__main__":
	print("Direct access not allowed...")
