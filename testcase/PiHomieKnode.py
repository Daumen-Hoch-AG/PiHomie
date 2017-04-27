#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import Bottle, PasteServer


class Node(Bottle):
	"""docstring for Node"""
	def __init__(self, name):
		super(Node, self).__init__()
		self.name = name
		self.route('/', callback=self.hello)


	def hello(self):
		return """
	<h1>Bottle is working !</h1>
	"""


if __name__ == '__main__':
	app = Node("Test")
	app.run(host='0.0.0.0', port=8080, server=PasteServer, debug=True)
