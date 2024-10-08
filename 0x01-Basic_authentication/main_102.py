#!/usr/bin/env python3
""" Main 102
"""
from api.v1.auth.auth import Auth

a = Auth()
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status*"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/usual", ["/api/v1/us*"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
