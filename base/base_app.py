#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from logging import INFO, WARNING, Formatter, getLogger, handlers
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
	if app.config['HOST']['NAME'] == 'node':
		app.config['UUID'] = open(app.config['HOST']['UUID_PATH']).read()


	# Logging

	# -- Standard
	standard_handler = handlers.RotatingFileHandler(app.config['LOGGING']['STANDARD'], maxBytes=1024 * 1024 * 100, backupCount=1)
	standard_handler.setLevel(INFO)
	standard_handler.setFormatter(Formatter('[%(asctime)s]%(levelname)s : %(message)s'))
	app.logger.addHandler(standard_handler)

	# -- Warnings und Errors
	warning_handler = handlers.RotatingFileHandler(app.config['LOGGING']['WARNING'], maxBytes=1024 * 1024 * 100, backupCount=1)
	warning_handler.setLevel(WARNING)
	warning_handler.setFormatter(Formatter('[%(asctime)s] %(levelname)s : %(message)s'))
	app.logger.addHandler(warning_handler)


	# -- SQL Database
	#---> Get SQLAlchemy Logger, ändern und binden an Flask
	sqlalchemy_logger = getLogger('sqlalchemy_logger')
	sql_handler = handlers.RotatingFileHandler(app.config['LOGGING']['SQL'], maxBytes=1024 * 1024 * 100, backupCount=1)
	# (lasse Config auf Modul-Standard...)
	sqlalchemy_logger.addHandler(sql_handler)
	

	# -- absolutes Loglevel (Minimum)
	app.logger.setLevel(INFO)


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
	

	app.logger.info("PiHomie Prozess wurde gestartet")
	
	return app
