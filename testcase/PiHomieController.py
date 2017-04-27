#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import Bottle, PasteServer
import requests


class Controller(Bottle):
	"""docstring for Controller"""
	def __init__(self, name):
		super(Controller, self).__init__()
		self.name = name
		self.route('/', callback=self.hello)
		self.route('/func', callback=self.hello2)


	def hello(self):
		r = requests.get("http://localhost:8888/")
		return r.text

	def hello2(self):
		r= requests.get("http://localhost:8888/func")
		return r.text

if __name__ == '__main__':
	app = Controller("Test")
	app.run(host='0.0.0.0', port=8080, server=PasteServer, debug=True)
