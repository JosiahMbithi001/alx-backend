#!/usr/binenv python3

""" LIFO Caching """
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFO Caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.last_key = ''
        
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key
        else:
            pass

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None 
    