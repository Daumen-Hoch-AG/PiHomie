#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Generic, os


class Reader(Generic.Sensor):
	"""Inhalte aus einer Datei lesen (Test-Sensor)"""

	def __init__(self, options, data):
		super(Generic.Sensor, self).__init__(options, data)
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
		return result_dict


	def getMainValue(self, options):
		"""Gesamter Inhalt der Datei"""
		with open( os.path.join(self.workspace, self.file), 'r' ) as f:
			return f.read()


	def getValue(self, options):
		"""Inhalt einer Zeile"""
		bezeichner = options.get('bezeichner', False)
		if not bezeichner:
			raise KeyError("Methode benötigt eine Option 'bezeichner' die die Zeilennummer angibt!")
		return self.getValuesAsDictionary( {'mode': 'one', 'start': bezeichner} )[bezeichner]


	def alert(self, data, options):
		"""Methode für proaktive Rückmeldung bei Änderung in der Datei"""
		# Check / Poll / ...
		#self.callback()
		pass



class Writer(Generic.Actor):
	"""Inhalt in eine Datei schreiben (Test-Aktor)"""

	def __init__(self, options, data):
		super(Generic.Actor, self).__init__(options, data)
		self.workspace = data.get('workspace', "/tmp")
		self.file = data.get('file', "ReadWriter"+str(self.id))


	def setAll(self, options, data):
		"""Inhalt in eine Datei (über-)schreiben"""
		payload = data.get('payload', False)
		if not payload:
			#TODO: Logeintrag
			raise KeyError("Methode benötigt Daten 'payload' für den Dateiinhalt!")
		else:
			with open(os.path.join(self.workspace, self.file), 'w') as f:
				return f.write(payload)


	def setValue(self, options, data):
		"""Inhalt an eine bestimmte Stelle in einer Datei schreiben"""
		linenumber = data.get("line", False)
		if not linenumber:
			#TODO: Logeintrag
			raise KeyError("Methode benötigt Daten in Verbindung mit einer Zeilennummer!")
		content = self.readItByLine()
		for line, payload in data.items():
			try:
				int(line)
				content[line] = payload
			except:
				#TODO: Logeintrag
				continue
		self.setAll({}, {'payload':content})
		return True


	def setValuesAsDictionary(self, options, data):
		"""Mehrere Inhalte an mehrere Stellen einer Datei schreiben"""
		content = self.readItByLine()
		for line, payload in data.items():
			try:
				int(line)
				content[line] = payload
			except:
				#TODO: Logeintrag
				continue
		self.setAll({}, {'payload': content})
		return True


	def readItByLine(self):
		"""Hilfsfunktion: Inhalt der Dateie in einem Zeilen-Dictionary"""
		result_dict = {}
		linenumber = 0
		with open(os.path.join(self.workspace, self.file), 'r') as f:
			for line in f:
				linenumber += 1
				result_dict[linenumber] = line
		return result_dict


if __name__ == "__main__":
	print("Direct access not allowed...")
