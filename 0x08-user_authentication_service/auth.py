#!/usr/bin/env python3
"""DB module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _generate_uuid() -> str:
    """uuid generator """
    return str(uuid.uuid4())


def _hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode(
            encoding='utf-8',
            errors='strict'),
        bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registering og user method"""
        try:
            userquery = self._db.find_user_by(email=email)
            if userquery:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            if email and password:
                obj = self._db.add_user(email, _hash_password(password))
                return obj

    def valid_login(self, email: str, password: str) -> bool:
        """ details verif"""
        try:
            obj = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(
                encoding='utf-8',
                errors='strict'), obj.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ create session method"""
        SessionId = None
        try:
            user = self._db.find_user_by(email=email)
            SessionId = _generate_uuid()
            self._db.update_user(user.id, session_id=SessionId)
        except NoResultFound:
            pass
        return SessionId

    def destroy_session(self, user_id: int):
        """delete session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass

    def get_user_from_session_id(self, session_id: str) -> User:
        """ data gathering of user"""
        Get_User = None
        try:
            Get_User = self._db.find_user_by(session_id=session_id)
        except Exception:
            pass
        return Get_User
