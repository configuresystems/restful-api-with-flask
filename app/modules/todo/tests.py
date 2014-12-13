from flask import url_for
from app.testing import BaseTestCase
import json


class TodoTests(BaseTestCase):
    def test_get_all_tasks(self):
        with self.client:
            response = self.client.get(url_for('get_tasks'))
            self.assert200(response)
            self.assertEqual(len(response.json.get('tasks')), 2)

    def test_get_task(self):
        with self.client:
            response = self.client.get(url_for('get_task', id=1))
            self.assert200(response)
            self.assertEqual(response.json.get('task')['title'],
                             "Test Sample Data")
