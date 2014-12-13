from flask import jsonify, url_for
from app import app
from app.dataset import DataSet


"""We need to ensure we have some data to use so we call the sample method
that we previously created"""
tasks = DataSet()
tasks = tasks.sample()


"""This here is some voodoo magic.  Basically, were replacing the id of
data's output to the URI that's used to access that object.  Doing this allows
us to easily interact with the objects we store"""
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            """When field equals id, make a new field within an empty dict,
            assign it to the URL by grabbing the 'get_task' route"""
            new_task['uri'] = url_for('get_task',
                                      id=task['id'],
                                      _external=True
                                      )
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    """Take the 'ToDo' objects we have stored in tasks and give us a handy URL
    """
    return jsonify({'tasks': map(make_public_task, tasks)})


@app.route('/todo/api/v1.0/tasks/<int:id>', methods=['GET'])
def get_task(id):
    """Unfortunately, lambda is still something I need to fully understand. I
    know whats going on here but I'm not the best at explaining it."""
    task = filter(lambda t: t['id'] == id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': make_public_task(task[0])})
