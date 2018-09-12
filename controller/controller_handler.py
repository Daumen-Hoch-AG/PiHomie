#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import current_app
from base.base_handler import BaseHandler
from controller.models import *


class Controller(BaseHandler):
	def __init__(self):
		super().__init__()
		self.db = db
		self.handler = {
			"test":self.handle_test,
			"init_node":self.init_node,
		}

		self.db.init_app(current_app)
		self.db.create_all()

	def init_node(self, options, data):
		#Dummy Response
		#Eigentlich: DB-> Ist Node vorhanden, wenn Ja, return Liste mit Noodles
		return {'options':{}, 'data':[{'type':'Writer','options':{'id':123},'data':{}}]}, 200

	def handle_test(self, data, request):
		current_app.logger.info("Test handled")
		return data, 200