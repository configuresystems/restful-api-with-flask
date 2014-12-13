from flask import url_for
from app.testing import BaseTestCase
import json


class TodoTests(BaseTestCase):
    def test_get_all_tasks(self):
        """Test intended to pull all tasks, ensure status 200 response,
        and that the list is a lenght of 2"""
        with self.client:
            tasks = [{'title': "Get Bread",
                      'description': "Wheat!"
                      },
                     {'title': "Get my To-Do List",
                      'description': "Check all of the items on my ToDo List"
                      }]
            for task in tasks:
                add = self.client.post(url_for('create_task'),
                                       headers={"Content-Type":
                                                "application/json"},
                                       data=json.dumps(task))
        with self.client:
            response = self.client.get(url_for('get_tasks'))
            self.assert200(response)
            self.assertEqual(len(response.json.get('tasks')), 2)

    def test_get_task(self):
        """Test indended to ensure status 200 and pull the task
        with an id of 1, then check its title"""
        with self.client:
            tasks = {'title': "Test Single Get",
                     'description': "Can we get it successfully"
                     }
            add = self.client.post(url_for('create_task'),
                                   headers={"Content-Type":
                                            "application/json"},
                                   data=json.dumps(tasks))
        with self.client:
            response = self.client.get(url_for('get_task', id=1))
            self.assert200(response)
            self.assertEqual(response.json.get('task')['title'],
                             "Test Single Get")

    def test_post_task(self):
        """Test the ability to post a new task to our ToDo list.
        We are testing for response 201, and content match, then we
        check to see what happens when you post invalid request.
        Repsonse 400
        """
        new_task = {'title': "I've created a post",
                    'description': "I should take a break"
                    }
        with self.client:
            response = self.client.post(url_for('create_task'),
                                        headers={"Content-Type":
                                                 "application/json"},
                                        data=json.dumps(new_task))
            self.assert_status(response, 201)
            self.assertEqual(response.json.get('task')['title'],
                             "I've created a post")

            """Test invalid POST request"""
            fail = self.client.post(url_for('create_task'),
                                    headers={"Content-Type":
                                             "application/json"},
                                    data=json.dumps({'titel':
                                                     "This should fail"})
                                    )
            self.assert400(fail)

    def test_update_task(self):
        """Test the ability to update our tasks"""
        new_task = {'title': "Test Updattin Tasks",
                    'description': "Let's ensure we can delete tasks"
                    }
        with self.client:
            add = self.client.post(url_for('create_task'),
                                   headers={"Content-Type":
                                            "application/json"},
                                   data=json.dumps(new_task))
            self.assert_status(add, 201)
            self.assertEqual(add.json.get('task')['title'],
                             "Test Updattin Tasks"
                             )
        with self.client:
            update = {'title': "Test Updating Tasks"}
            fix = self.client.put(url_for('update_task',
                                          id=1),
                                  headers={"Content-Type":
                                           "application/json"},
                                  data=json.dumps(update))
            self.assert200(fix)

    def test_delete_tasks(self):
        """Test to ensure we can delete data"""
        new_task = {'title': "Test Deleting Tasks",
                    'description': "Let's ensure we can delete tasks"
                    }
        with self.client:
            add = self.client.post(url_for('create_task'),
                                   headers={"Content-Type":
                                            "application/json"},
                                   data=json.dumps(new_task))
            self.assert_status(add, 201)
            self.assertEqual(add.json.get('task')['title'],
                             "Test Deleting Tasks"
                             )
        with self.client:
            response = self.client.delete(url_for('reset_task',
                                          id=add.json.get('id')))
            self.assert200(response)
            self.assertEqual(len(response.json.get('tasks')), 0)
