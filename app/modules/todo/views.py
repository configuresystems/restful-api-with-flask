from flask import jsonify, url_for, request, abort
from app import app
from app.dataset import DataSet


"""We need to ensure we have some data to use so we call the sample method
that we previously created"""
tasks = DataSet(data=[])
tasks = tasks.data

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


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    id = 1
    if len(tasks) > 0:
        id = tasks[-1]['id'] + 1
    task = {'id': id,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
            }
    tasks.append(task)
    return jsonify({'task': make_public_task(task)}), 201


@app.route('/todo/api/v1.0/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = filter(lambda t: t['id'] == id, tasks)
    if len(task) == 0:
        abort(400)
    if not request.json:
        abort(400)
    if 'title' in request.json \
       and type(request.json['title']) is not unicode:
        abort(400)
    if 'description' in request.json \
       and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json \
       and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description',
                                              task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': make_public_task(task[0])})


@app.route('/todo/api/v1.0/tasks/reset', methods=['DELETE'])
@app.route('/todo/api/v1.0/tasks/<int:id>/reset', methods=['DELETE'])
def reset_task(id=None):
    if not id:
        for task in tasks:
            tasks.remove(task)
        return jsonify({'tasks': map(make_public_task, tasks)})
    task = filter(lambda t: t['id'] == id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'deleted': task})
