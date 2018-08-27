#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import os, configparser


def create_app():
	app = Flask(__name__)
	app.secret_key=os.urandom(24)

	app.config['BaseDir'] = os.path.dirname(os.path.realpath(__file__))

	################
    # Config lesen #
    ################
	config = configparser.ConfigParser()
	cfg_file = os.path.join(app.config['BaseDir'],'config.ini')
	config.read(cfg_file)

	if config['BASE']['Type'].upper() == "CONTROLLER":
		from handler.controller_handler import Controller as Host
	elif config['BASE']['Type'].upper() == "KNODE":
		from handler.knode_handler import Knode as Host
	
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
