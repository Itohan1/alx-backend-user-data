#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
check = getenv("AUTH_TYPE")

if check == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def check_again():
    """Check request authentication"""
    if auth is None:
        return

    check_list = ['/api/v1/status/',
                  '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth.require_auth(request.path, check_list) is not True:
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def request_unfound(error) -> str:
    """Handle failed request"""

    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def deny_access(error) -> str:
    """Response for error handler for failed authentication"""

    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
