#!/usr/bin/env python3
"""
Main file
"""


def index_range(page, page_size):
    """index_range function"""

    return ((page-1) * page_size, page*page_size)
