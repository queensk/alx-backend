#!/usr/bin/env python3
"""
FIFO caching
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        initialize
        """
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.queue:
                del_key = self.queue.popleft()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        value = self.cache_data.get(key)
        return value
