# https://skillsmart.ru/algo/py-kf32y/z1467b2a4244.html

class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.elements_count = 0

    def hash_fun(self, key):
        return sum(key.encode()) % self.size

    def put(self, key, value):
        hash_index = self.hash_fun(key)
        step = 3
        rarely_used_key = min(self.hits)
        while step < self.size:
            if self.elements_count == self.size:
                if self.hits[hash_index] == rarely_used_key:
                    self.keys[hash_index] = None
                    self.values[hash_index] = None
                    self.hits[hash_index] = 0
                    self.elements_count -= 1
            if self.keys[hash_index] is None:
                self.keys[hash_index] = key
                self.values[hash_index] = value
                self.hits[hash_index] += 1
                self.elements_count += 1
                break
            hash_index += step-1
            if hash_index > self.size-1:
                hash_index = abs(hash_index-self.size-1)
                step += 1
    
    def get(self, key):
        hash_index = self.hash_fun(key)
        if self.keys[hash_index] == key:
            self.hits[hash_index] += 1
            return self.values[hash_index]
        else:
            for hash_index in range(self.size):
                if self.keys[hash_index] == key:
                    self.hits[hash_index] += 1
                    return self.values[hash_index]
        return None
