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
			"test":self.handle_test
		}

		self.db.init_app(current_app)
		self.db.create_all()

	def handle_test(self, data):
		current_app.logger.info("Test handled")# ohne Wirkung bisher
		return data, 200