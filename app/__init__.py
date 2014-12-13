from flask import Flask


# instantiate Flask so that we may use it!
app = Flask(__name__)

# Set our application constants via a config.py object
app.config.from_object('config.DevConfiguration')

# Import our master views file
from app import views
