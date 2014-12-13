from flask.ext.testing import TestCase
from flask import url_for
from app import app, views


class BaseTestCase(TestCase):
    """Our first unittest to check the response code, payload type, and payload
    """
    def create_app(self):
        """Here we can set application configurations so flag our application
        as testing, in case we build verbose functions or something"""
        app.config.from_object('config.TestingConfiguration')
        return app
