#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import os, configparser


def create_app(Host):
	app = Flask("PiHomie")
	app.secret_key=os.urandom(24)

	app.config['BaseDir'] = os.path.dirname(os.path.realpath(__file__))

	################
    # Config lesen #
    ################
	config = configparser.ConfigParser()
	cfg_file = os.path.join(app.config['BaseDir'],'config.ini')
	config.read(cfg_file)

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
