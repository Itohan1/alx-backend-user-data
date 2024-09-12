#!/usr/bin/env python3
"""End-to-end integration test"""
import requests


def register_user(email: str, password: str) -> None:
    """User registeration"""
    url = 'http://localhost:5000/users'
    data = {
        'email': email,
        'password': password
    }

    try:
        response = requests.post(url, data=data)
        assert response.status_code == 200
        print(response.json())
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


def log_in_wrong_password(email: str, password: str) -> None:
    """Log in with wrong password"""

    url = 'http://localhost:5000/sessions'
    data = {
        'email': email,
        'wrong_password': password
    }

    try:
        response = requests.post(url, data=data)

        assert response.status_code == 401
        print("Wrong password")
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


def log_in(email: str, password: str) -> str:
    """Log in sessions"""

    url = 'http://localhost:5000/sessions'
    data = {
        'email': email,
        'wrong_password': password
    }

    try:
        response = requests.post(url, data=data)

        assert response.status_code == 200
        print(response.json())
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


def profile_unlogged() -> None:
    """Profile unlogged"""

    url = 'http://localhost:5000/profile'

    try:
        response = request.get(url)
        assert response.status_code == 403
        print("Profile unlogged")
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


def profile_logged(session_id: str) -> None:
    """Profile logged"""

    url = 'http://localhost:5000/profile'

    data = {"session_id": session_id}
    try:
        response = request.get(url, data=data)
        assert response.status_code == 200
        print(response.json())
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


def log_out(session_id: str) -> None:
    """Sessions logged out"""

    url = 'http://localhost:5000/logout'

    data = {"session_id": session_id}
    try:
        response = request.delete(url, data=data)
        assert response.status_code == 200
        print(response.json())
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


def reset_password_token(email: str) -> str:
    """Reset password token"""

    url = 'http://localhost:5000/reset_password'

    data = {"email": email}
    try:
        response = request.post(url, data=data)
        assert response.status_code == 200
        print(response.json())
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


def update_password(
        email: str, reset_token: str, new_password: str) -> None:
    """Update password end-point"""
    url = 'http://localhost:5000/reset_password/reset_password'

    data = {"email": email}
    try:
        response = request.put(url, data=data)
        assert response.status_code == 200
        print(response.json())
    except AssertionError:
        print("Request failed")
    except requests.exceptions.RequestException:
        print(f"Could not fetch request")
    return None


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
