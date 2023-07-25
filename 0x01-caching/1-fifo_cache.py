#!/usr/bin/env python3
""" FIFO caching """

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """This Class Inherits Base Caching"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = sorted(self.cache_data)[0]
                self.cache_data.pop(first)
                print("DISCARD: {}".format(first))
        else:
            pass
    
    def get(self, key):
        """This Function returns the value of given key"""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None