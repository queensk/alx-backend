#!/usr/bin/python3
"""
LIFO Caching
"""
BaseCaching = __import__('base_cache').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching
    """

    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.stack:
                del_key = self.stack.pop()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        value = self.cache_data.get(key)
        return value
