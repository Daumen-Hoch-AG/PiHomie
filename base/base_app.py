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

	# Logging
	standardlog_handler = RotatingFileHandler('pihomie.log', maxBytes=1024 * 1024 * 100, backupCount=1)
	standardlog_handler.setLevel(logging.INFO)
	standardlog_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s : %(message)s'))
	app.logger.addHandler(standardlog_handler)
	"""
	# ---- ???
	sqlalchemy_logger = logging.getLogger('sqlalchemy_logger')
	sql_handler = RotatingFileHandler('sqlalchemy.log', maxBytes=1024 * 1024 * 100, backupCount=1)
	# (lasse Config auf Modul-Standard...)
	sqlalchemy_logger.addHandler(sql_handler)
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
