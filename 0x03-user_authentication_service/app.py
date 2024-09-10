#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def check_form():
    """Flask app that has a single GET route"""

    return jsonify({})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
