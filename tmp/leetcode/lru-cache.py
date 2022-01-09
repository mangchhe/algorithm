from collections import OrderedDict

class LRUCache(object):
    
    capacity = 0
    o = []

    def __init__(self, capacity):
        self.capacity = capacity
        self.o = OrderedDict()

    def get(self, key):
        if key not in self.o:
            return -1
        v = self.o.pop(key)
        self.o[key] = v
        return v

    def put(self, key, value):
        if key in self.o:
            self.o.pop(key)
        elif len(self.o) == self.capacity:
            self.o.popitem(last=False)
        self.o[key] = value
