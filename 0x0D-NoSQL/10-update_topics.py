#!/usr/bin/env python3
""" update one query by name topics is a list"""


def update_topics(mongo_collection, name, topics):
    """up tocis """
    query = {"name": name}
    up = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, up)
