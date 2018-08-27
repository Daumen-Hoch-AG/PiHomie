#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import os, configparser


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
