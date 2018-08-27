#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import os, configparser, logging


def create_app(Host, config_path):
	app = Flask("PiHomie")
	app.secret_key=os.urandom(24)

	#
	# The path to the instance folder can be found via the Flask.instance_path. Flask also provides a shortcut to open a file from the instance folder with Flask.open_instance_resource().
	#
	################
	# Config lesen #
	################
	config = configparser.ConfigParser()
	config.read(config_path)

	app.config['BaseDir'] = os.path.dirname(os.path.realpath(__file__))
	app.config['FILE'] = config

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
