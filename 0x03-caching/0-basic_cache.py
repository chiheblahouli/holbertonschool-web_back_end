#!/usr/bin/python3
""" BaseCaching """
BasicCaching = __import__('base_caching').BaseCaching


class BasicCache(BasicCaching):
    """basic cache class"""

    def put(self, key, item):
        """put function"""
        if key and item:
            self.cache_data[str(key)] = item

    def get(self, key):
        """get function"""
        if key:
            return self.cache_data.get(key)
        else:
            return None
