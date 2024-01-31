#!/usr/bin/env python3
""" module for the class MRUCache """

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ LRU caching system that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        add an item to the cache - when cache is full, discards in MRU
        """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys[-1])
                    print('DISCARD:', self.keys[-1])
                    self.keys.pop(-1)
                if key not in self.keys:
                    self.keys.append(key)

    def get(self, key):
        """ retrieve an item from the cache """
        value = self.cache_data.get(key, None)
        if value:
            self.keys.remove(key)
            self.keys.append(key)
        return value
