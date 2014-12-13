

class DataSet():
    """Since we're not using a database for this exercise, we will need an
    object to store it, so that we can play with that data"""
    def __init__(self, data=[]):
        self.data = data

    def sample(self):
        """Create a set of sample data for quick testing
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
        """
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
