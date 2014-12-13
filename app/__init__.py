from flask import Flask, jsonify


# instantiate Flask so that we may use it!
app = Flask(__name__)

# this is our index route, found here
# DEFAULT: http://[hostname]:5000/hello-world


@app.route('/hello-world')
def index():
    return jsonify({"message": "Hello World!"})
