#!/usr/bin/python3
""" FIFOCache """
BasicCaching = __import__('base_caching').BaseCaching


class FIFOCache(BasicCaching):
    """FIFOCache class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key and item:
            if len(self.cache_data) >= BasicCaching.MAX_ITEMS and str(
                    key) not in self.cache_data:
                discarded = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(discarded))
                self.cache_data.pop(discarded)
            self.cache_data[str(key)] = item

    def get(self, key):
        """get function"""
        if key:
            return self.cache_data.get(key)
        else:
            return None
