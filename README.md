RESTful API with Flask and Flask-Testing
================

##### Version: 0.1

# Overview

Part 1:  We will install Flask and create "Hello World" response to
ensure our environment is built and configured properly.

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

```base
├── app
│   ├── __init__.py
│   └── testing.py
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```

### Line count

2 ./requirements.txt
20 ./LICENSE
89 ./README.md
8 ./run.py
13 ./app/__init__.py
27 ./app/testing.py
159 total

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
git clone -b part-1 \
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
#### Output should look like so
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.009s
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
| GET | JSON | http://[hostname]/hello-world | Retrieve "Hello World" |

```bash
curl -i http://[hostname]/hello-world:5000
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 32
Server: Werkzeug/0.9.6 Python/2.7.6
Date: Sat, 13 Dec 2014 01:02:35 GMT

{
      "message": "Hello World!"
}
```

