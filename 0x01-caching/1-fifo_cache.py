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
        Initializes the cache data and a queue to keep track of the order of items
        """
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discarded = self.queue.popleft()
                print(f"DISCARD: {discarded}")
                del self.cache_data[discarded]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value associated with the key in self.cache_data
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
