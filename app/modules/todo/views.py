from flask import jsonify, url_for
from app import app
from app.dataset import DataSet


# this is our index route, found here
# DEFAULT: http://[hostname]:5000/hello-world


tasks = DataSet()
tasks = tasks.sample()


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task',
                                      id=task['id'],
                                      _external=True
                                      )
        else:
            new_task[field] = task[field]
    return new_task


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': map(make_public_task, tasks)})


@app.route('/todo/api/v1.0/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = filter(lambda t: t['id'] == id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': make_public_task(task[0])})
