#!/usr/bin/env python3
"""
    A new Flask view that handles
    all routes for the Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
import os
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def sess_first() -> str:
    """Session authentication"""

    from api.v1.views.users import User
    from api.v1.app import auth

    e_details = request.form.get('email')
    p_details = request.form.get('password')

    if not e_details:
        return jsonify({"error": "email missing"}), 400

    if not p_details:
        return jsonify({"error": "password missing"}), 400

    check_email = User.search({"email": e_details})

    if not check_email or len(check_email) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = check_email[0]
    check_valid = user.is_valid_password(p_details)

    if not check_valid:
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)

    name = os.getenv('SESSION_NAME')
    result = jsonify(user.to_json())
    result.set_cookie(name, session_id)

    return result


@app_views.route(
        '/auth_session/logout', methods=['DELETE'],
        strict_slashes=False)
def del_login() -> Tuple[str, int]:
    """Destroy session"""

    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)

    if not destroy_session:
        abort(404)

    return jsonify({}), 200
