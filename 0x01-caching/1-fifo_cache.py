#!/usr/bin/env python3
""" module for the class FIFOCache """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system that inherits from BaseCaching """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        add an item to the cache - when cache is full, discards in FIFO
        """
        if key and item and self.get(key) != item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key = next(iter(self.cache_data))
                self.cache_data.pop(key)
                print('DISCARD:', key)

    def get(self, key):
        """ retrieves an item from the cache """
        return self.cache_data.get(key, None)
