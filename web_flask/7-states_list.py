#!/usr/bin/python3
"""Starts  a Flask web application.
 The application listens on 0.0.0.0, port 5000.
 Routes:
         /states_list: HTML page with a list of all state objects in DBStorage.
"""
from models import storage
from flask import Flask


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def:
    """ """
    return

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
