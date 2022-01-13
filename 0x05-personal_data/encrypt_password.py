#!/usr/bin/env python3
"""
hashing
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    hashpwd
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid function"""
    return bcrypt.checkpw(password.encode(), hashed_password)
