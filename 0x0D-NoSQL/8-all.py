#!/usr/bin/env python3
""" task 8 List all documents"""


def list_all(mongo_collection):
    """list all colllection's docuemts"""
    return mongo_collection.find()
