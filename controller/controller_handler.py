from .base_handler import BaseHandler

class Controller(BaseHandler):
    def __init__(self):
        super().__init__()
        self.handler = {
            "test":self.handle_test
        }

    def handle_test(self, data):
        return data, 200