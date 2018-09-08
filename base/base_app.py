#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import os, logging


def create_app(Host, config_path):
	app = Flask("PiHomie")
	app.secret_key=os.urandom(24)

	################
	# Config lesen #
	################
	app.config.from_json(config_path)
	app.config['BaseDir'] = os.path.dirname(os.path.realpath(__file__))
	app.config['PRIVCERT'] = os.path.join(app.config['BaseDir'],app.config['PRIVCERT'])
	app.config['CLIENTCERTDIR'] = os.path.join(app.config['BaseDir'],app.config['CLIENTCERTDIR'])

	"""
	infoHandler = logging.FileHandler(app.config['FILE']['logging']['info'])
	infoHandler.setLevel(logging.INFO)
	app.logger.addHandler(infoHandler)
	
	warnHandler = logging.FileHandler(app.config['FILE']['logging']['warning'])
	warnHandler.setLevel(logging.WARNING)
	app.logger.addHandler(warnHandler)
	errHandler = logging.FileHandler(app.config['FILE']['logging']['error'])
	errHandler.setLevel(logging.ERROR)
	app.logger.addHandler(errHandler)
	"""

	# Host Objekt initialiseren und Config übergeben
	with app.app_context():
		host = Host()

	@app.route("/api")
	def api():
		#Response verarbeiten
		response, code = host.handle_request(request)
		if len(response) > 0:
			return jsonify(response), code
		else:
			return '', code
	
	return app
