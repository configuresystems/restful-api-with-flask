from flask import url_for
from app.testing import BaseTestCase
import json


class TodoTests(BaseTestCase):
    def test_get_all_tasks(self):
        """Test intended to pull all tasks, ensure status 200 response,
        and that the list is a lenght of 2"""
        with self.client:
            response = self.client.get(url_for('get_tasks'))
            self.assert200(response)
            self.assertEqual(len(response.json.get('tasks')), 2)

    def test_get_task(self):
        """Test indended to ensure status 200 and pull the task
        with an id of 1, then check its title"""
        with self.client:
            response = self.client.get(url_for('get_task', id=1))
            self.assert200(response)
            self.assertEqual(response.json.get('task')['title'],
                             "Test Sample Data")
