#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from bottle import Bottle, BaseRequest, PasteServer, run


#class Communicator(threading.Thread):
class Steuerung(Bottle):
	"""Test Bottle"""
	def __init__(self, port=8100):
		super(Steuerung, self).__init__()
		self.port = port
		
		# Global Variables
		os.chdir(os.path.dirname(os.path.realpath(__file__)))


	#def run(self):
		# starten des Bottle Servers
#		self.startServer()


	def _route(self):
		self._app.route("/", callback=self.welcome)


	# Routings
	def welcome(self):
		return """
	<h1>Bottle is working !</h1>
	<h2>Synchronisierungsserver für die TeacherTab WebApp</h2>
	<p>Derzeitige Funktionen :</p>
	<ul style="outline: 1px solid blue;display: inline-block;padding: 1em 2em;margin: 1em;">
	<li>/ShowAll</li>
	<li>/HowAreYou</li>
	<li>/storeFromClient</li>
	<li>/giveToClient</li>
	<li>/deleteStudentOnServer</li>
	<li>/deleteKlasse</li>
	<li>/pdf_export</li>
	<li>/checkDB</li>
	</ul>
	<p style="font-size: 0.75em;text-align: center;margin-top: 3em;">WebApp unter <a href="http://www.teachertab.de/WebApp">TeacherTab.de/WebApp</p>
	"""

	def startServer(self):
		# Settings und Service-Start
		BaseRequest.MEMFILE_MAX = 102400
		run(self._app, host='0.0.0.0', port=self.port, server=PasteServer, debug=True)


	def testing(self):
		print
		print "Testing ist DAAA !"
		print



class Knoten(object):
	"""docstring for Knoten"""
	def __init__(self, name):
		super(Knoten, self).__init__()
		self.name = name
		self.devices = {}
		
		# Status
		self.status = False

	def createChilds(self, devicelist):
		for device in devicelist:
			self.devices[device[0]] = device[1]()
		self.status = True
