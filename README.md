RESTful API with Flask and Flask-Testing
================

##### Version: 0.3

# Overview

Part 1:  We will install Flask and create "Hello World" response to
ensure our environment is built and configured properly.

Part 2:  Start structuring our framework, creating our GET endpoints,
and creating new unittests to ensure our changes dont break anything

Part 3:  Conjure methods for submitting new tasks, updating tasks, and
deleting tasks

# Requirements

Aptitude Packages:

- git
- python-dev
- build-essentials
- python-setuptools
- python-virtualenv

Required PIP package, also in the requirements.txt

- Flask==0.10.1
- Flask-Testing==0.4.2

# Project Directory Structure

```bash
├── app
│   ├── dataset.py
│   ├── __init__.py
│   ├── modules
│   │   ├── __init__.py
│   │   └── todo
│   │       ├── __init__.py
│   │       ├── tests.py
│   │       └── views.py
│   ├── testing.py
│   └── views.py
├── config.py
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```

### Line Count

```bash
20 ./LICENSE
39 ./config.py
132 ./README.md
8 ./run.py
0 ./app/modules/__init__.py
112 ./app/modules/todo/tests.py
0 ./app/modules/todo/__init__.py
98 ./app/modules/todo/views.py
11 ./app/__init__.py
24 ./app/testing.py
3 ./app/views.py
45 ./app/dataset.py
494 total
```

# Installation

### Ubuntu

```bash
sudo apt-get update
# Next two lines are one command
sudo apt-get install git python-dev build-essential python-setuptools \
python-virtualenv
```

### Setup Environment

```bash
# The next three lines are one command
git clone -b part-3 \
https://github.com/configuresystems/restful-api-with-flask.git \
application
# Next command
cd application
virtualenv flask
source flask/bin/activate
pip install -r requirements.txt
```

Run tests to ensure its all working well

```bash
python -m unittest discover
#.....
#----------------------------------------------------------------------
#Ran 5 tests in 0.030s
#
#OK
```

Run a usage Flask instance

```bash
# The run.py file declares Flask is listening on all interfaces so you
# can use any accessible IP of the instance running our app
python run.py
```

# Usage

|  HTTP Method | Response|  URI |  Action |
| :-----------:|:--:| :--- | :------ |
| GET | JSON | http://[hostname]:5000/todo/api/v1.0/tasks | Retrieve a list of our tasks |
| GET | JSON | http://[hostname]:5000/todo/api/v1.0/tasks/<int:id> | Retrieve a task by ID |
| POST | JSON | http://[hostname]:5000/todo/api/v1.0/tasks | Create a new task |
| PUT | JSON | http://[hostname]:5000/todo/api/v1.0/tasks/<int:id> | Update task by id |
| DELETE | JSON | http://[hostname]:5000/todo/api/v1.0/tasks/<int:id> | Delete task by id |

### Get All Tasks

```bash
curl -i http://[hostname]:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 390
Server: Werkzeug/0.9.6 Python/2.7.6
Date: Sat, 13 Dec 2014 05:36:09 GMT

{
  "tasks": [
    {
      "description": "Write unittests to valid!",
      "done": false,
      "title": "Test Sample Data",
      "uri": "http://[hostname]:5000/todo/api/v1.0/tasks/1"
    },
    {
      "description": "Write a PUT method",
      "done": false,
      "title": "Learn how to update entries",
      "uri": "http://[hostname]:5000/todo/api/v1.0/tasks/2"
    }
  ]
}
```

### Get Single Task

```bash
curl -i http://[hostname]:5000/todo/api/v1.0/tasks/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 181
Server: Werkzeug/0.9.6 Python/2.7.6
Date: Sat, 13 Dec 2014 05:36:36 GMT

{
  "task": {
    "description": "Write unittests to valid!",
    "done": false,
    "title": "Test Sample Data",
    "uri": "http://[hostname]:5000/todo/api/v1.0/tasks/1"
  }
}
```
