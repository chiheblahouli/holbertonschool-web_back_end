#!/usr/bin/env python3
""" schools_by_topic file"""


def schools_by_topic(mongo_collection, topic):
    """ search with topics """
    return mongo_collection.find({"topics": topic})
