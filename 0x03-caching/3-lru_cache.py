#!/usr/bin/python3
""" FIFOCache """
BasicCaching = __import__('base_caching').BaseCaching


class LRUCache(BasicCaching):
    """FIFOCache class"""
    cachearray = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put function"""
        lenstoreD_cache = len(self.cache_data)
        if key and item:
            self.cache_data[key] = item
            if key not in self.cachearray:
                self.cachearray.append(key)
            else:
                self.cachearray.append(
                    self.cachearray.pop(self.cachearray.index(key)))
            if lenstoreD_cache > BasicCaching.MAX_ITEMS:
                firselemt = self.cachearray[0]
                self.cachearray.pop(0)
                self.cache_data.pop(firselemt)
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """get function"""
        if key:
            return self.cache_data.get(key)
        else:
            return None
