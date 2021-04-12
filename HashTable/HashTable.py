# https://skillsmart.ru/algo/py-kf32y/re8af6c877.html

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step_size = stp
        self.slots = [None] * self.size
    
    def hash_fun(self, value):
        return sum(value.encode()) % self.size

    def seek_slot(self, value):
        hash_index = self.hash_fun(value)
        step = self.step_size
        while step < self.size:
            if self.slots[hash_index] is None:
                return hash_index
            hash_index += step-1
            if hash_index > self.size-1:
                hash_index = abs(hash_index-self.size-1)
                step += 1
        return None

    def put(self, value):
        hash_index = self.seek_slot(value)
        if hash_index is not None:
            self.slots[hash_index] = value
            return hash_index
        return None

    def find(self, value):
        hash_index = self.hash_fun(value)
        step = self.step_size
        while step < self.size:
            if self.slots[hash_index] == value:
                return hash_index
            hash_index += step-1
            if hash_index > self.size-1:
                hash_index = abs(hash_index-self.size-1)
                step += 1
        return None
