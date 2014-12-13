

class DataSet():
    def __init__(self, data=[]):
        self.data = data

    def sample(self):
        self.data = [{
            'id': 1,
            'title': u'Test Sample Data',
            'description': u'Write unittests to valid!',
            'done': False
            }, {
            'id': 2,
            'title': u'Learn how to update entries',
            'description': u'Write a PUT method',
            'done': False
            }]
        return self.data
