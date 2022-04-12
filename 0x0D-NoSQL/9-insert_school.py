#!/usr/bin/env python3
""" insert to school"""


def insert_school(mongo_collection, **kwargs):
    """insert into school collection NoSQL"""
    return mongo_collection.insert_one(kwargs).inserted_id
