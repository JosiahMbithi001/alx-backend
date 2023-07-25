
""" Basic dictionary"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """This Class will inherit from BaseCaching"""
    def __init__(self):
        """Constructor"""
        super().__init__()
    
    def put(self, key, item):
        """Assign to the dictionary"""
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """Return the value linked to the key"""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

