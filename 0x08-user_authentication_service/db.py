#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ methode to add user"""
        User_obj = User()
        User_obj.email = email
        User_obj.hashed_password = hashed_password
        self._session.add(User_obj)
        self._session.commit()
        return User_obj

    def find_user_by(self, **args) -> User:
        """find User args"""
        user_obj = self._session.query(User).filter_by(**args).first()
        if user_obj is None:
            raise NoResultFound
        return user_obj

    def update_user(self, user_id: int, **ards) -> None:
        """update_user methode"""
        try:
            self._session.query(User).filter(
                User.id == user_id).update(ards)
        except BaseException:
            raise ValueError
