#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import Bottle, PasteServer


class Controller(Bottle):
	"""docstring for Controller"""
	def __init__(self, name):
		super(Controller, self).__init__()
		self.name = name
		self.route('/', callback=self.hello)


	def hello(self):
		return """
	<h1>Bottle is working !</h1>
	"""


if __name__ == '__main__':
	app = Controller("Test")
	app.run(host='0.0.0.0', port=8080, server=PasteServer, debug=True)
