from flask.ext.testing import TestCase
from flask import url_for
from app import app


class HelloWorldTest(TestCase):
    """
    Our first unittest to check the response code, payload type, and payload
    """
    def create_app(self):
        """
        Here we can set application configurations so flag our application
        as testing, in case we build verbose functions or something
        """
        app.config['TESTING'] = True
        return app

    def test_hello_world(self):
        """
        We test three things against the index route
        reponse code == 200
        response.message = "Hello World!"
        response payload is JSON
        """
        with self.client:
            response = self.client.get(
                    url_for('index')
                    )
            # is it a 200 response
            self.assert200(response)
            # is the payload a JSON document
            self.assertTrue(isinstance(response.json, dict))
            # does the message contain the phrase, Hello World!
            self.assertEqual(response.json['message'], "Hello World!")
