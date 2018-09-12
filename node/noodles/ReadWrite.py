#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .Generic import Sensor, Actor
import os


class Reader(Sensor):
	"""Inhalte aus einer Datei lesen (Test-Sensor)"""

	def __init__(self, options, data, callback):
		super().__init__(options, data, callback)
		self.workspace = data.get('workspace', "/tmp")
		self.file = data.get('file', "ReadWriter"+str(self.id))


	def getValuesAsDictionary(self, options):
		"""Inhalt der Dateie in einem Zeilen-Dictionary"""
		result_dict = {}
		linenumber = 0
		mode = options.get('mode', "all")
		startLine = options.get('start', False)
		endLine = options.get('end', False)
		with open( os.path.join(self.workspace, self.file), 'r' ) as f:
			for line in f:
				linenumber += 1
				if mode == "range":
					if linenumber >= startLine and linenumber <= endLine:
						result_dict[linenumber] = line
				elif mode == "one":
					if linenumber == startLine:
						result_dict[linenumber] = line
				else:
					result_dict[linenumber] = line
		return result_dict, 200


	def getMainValue(self, options):
		"""Gesamter Inhalt der Datei"""
		with open( os.path.join(self.workspace, self.file), 'r' ) as f:
			result = f.read()
		return {'result':result}, 200


	def getValue(self, options):
		"""Inhalt einer Zeile"""
		bezeichner = options.get('bezeichner', False)
		if not bezeichner:
			raise KeyError("Methode benötigt eine Option 'bezeichner' die die Zeilennummer angibt!")
		return self.getValuesAsDictionary( {'mode': 'one', 'start': bezeichner} ), 200


	def alert(self, data, options):
		"""Methode für proaktive Rückmeldung bei Änderung in der Datei"""
		# Check / Poll / ...
		#self.callback()
		pass



class Writer(Actor):
	"""Inhalt in eine Datei schreiben (Test-Aktor)"""

	def __init__(self, options, data, callback):
		super().__init__(options, data, callback)
		self.workspace = data.get('workspace', "/tmp")
		self.file = data.get('file', "ReadWriter"+str(self.id))


	def setAll(self, options, data):
		"""Inhalt in eine Datei (über-)schreiben"""
		payload = data.get('payload', False)
		if not payload:
			raise KeyError("Methode benötigt Daten 'payload' für den Dateiinhalt!")
		else:
			with open(os.path.join(self.workspace, self.file), 'w') as f:
				f.write(payload)
				return {}, 200


	def setValue(self, options, data):
		"""Inhalt an eine bestimmte Stelle in einer Datei schreiben"""
		#TODO: Datei anlegen und Leerzeilen erstellen, wenn noch nicht vorhanden
		r = self.setValuesAsDictionary(options, data)
		return ({}, 200) if r else ({}, 400)


	def setValuesAsDictionary(self, options, data):
		"""Mehrere Inhalte an mehrere Stellen einer Datei schreiben"""
		#TODO: Zeilen an Datei anfügen mit Leerzeilen wenn zu wenig
		path = os.path.join(self.workspace, self.file)
		if os.path.exists(path):
			linenumber = 0
			new_content = list()
			with open(path, 'r') as f:
				for line in f:
					linenumber += 1
					if str(linenumber) in data.keys():
						new_content.append(data[str(linenumber)])
					else:
						new_content.append(line)
			
			with open(path, 'w') as f:
				for line in new_content:
					f.write(line)
		else:
			raise IOError("Die Datei existiert noch nicht")

		return {}, 200



if __name__ == "__main__":
	print("Direct access not allowed...")
