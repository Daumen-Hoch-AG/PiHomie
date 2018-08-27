from base.base_handler import BaseHandler
from flask import current_app

class Controller(BaseHandler):
	def __init__(self):
		super().__init__()
		self.handler = {
			"test":self.handle_test
		}

	def handle_test(self, data):
		current_app.logger.info("Test handled")
		return data, 200