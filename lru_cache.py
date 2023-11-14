from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity=16):
        self.cache = OrderedDict()
        self.capacity = capacity

    def put(self, key, value):
        if key in self.cache.keys():
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def get(self, key):
        try:
            return self.cache[key]
        except KeyError:
            return None


cache = LRUCache()
for i in range(20):
    cache.put(i, i)
for i in range(len(cache.cache)):
    print(cache.get(i))
cache.put(1, 3)
cache.put(2, 3)
cache.put(3, 3)
print(cache.get(3))
print(cache.get(4))
