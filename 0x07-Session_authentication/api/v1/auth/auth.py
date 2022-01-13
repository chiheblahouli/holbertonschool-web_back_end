#!/usr/bin/env python3
"""
auth class
"""
from flask import Flask, jsonify, abort, request
from typing import List, TypeVar


class Auth:
    """ User Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth funct"""
        if path is None or excluded_paths is None:
            return True
        path = path + "/" if path[-1] != "/" else path
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ auth header """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ current User"""
        return None
