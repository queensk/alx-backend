#!/usr/bin/env python3
"""
Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Assigns the item value to the key in self.cache_data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value associated with the key in self.cache_data
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
