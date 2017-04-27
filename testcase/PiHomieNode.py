#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import Bottle, PasteServer
from zWaveDummy import ZWaveDummy


class Node(Bottle):
	"""docstring for Node"""
	def __init__(self, name):
		super(Node, self).__init__()
		self.name = name
		self.route('/', callback=self.hello)
		self.route('/func', callback=self.hello2)
		self.zwave = ZWaveDummy()


	def hello(self):
		self.zwave.put("Ein Kommando vom Node!")
		return """
	<h1>Bottle is working !</h1>
	"""

	def hello2(self):
		self.zwave.addToQueue("Ein Kommando vom Node - Funktion!")
		return "-"


if __name__ == '__main__':
	app = Node("Test")
	app.run(host='0.0.0.0', port=8888, server=PasteServer, debug=True)
