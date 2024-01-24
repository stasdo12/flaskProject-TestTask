from flask import jsonify

import app

#Хорошая практика ерор хендлер не вышло
class ProductNotFound(Exception):
    status_code = 404

    def init(self, message, status_code=None, payload=None):
        Exception.init(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

