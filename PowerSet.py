# https://skillsmart.ru/algo/py-kf32y/s83e6f8ef537.html

class PowerSet:

    def __init__(self):
        self.sz = 373
        self.slots = [[] for i in range(self.sz)]
        self.count = 0

    def hash(self, value):
        return sum(value.encode()) % self.sz
    
    def size(self):
        return self.count

    def put(self, value):
        # O(m), where m = len(i)
        i = self.hash(value)
        if value not in self.slots[i]:
            self.slots[i].append(value)
            self.count += 1

    def get(self, value):
        # O(m), where m = len(i)
        i = self.hash(value)
        if value in self.slots[i]: 
            return True
        return False

    def remove(self, value):
        # O(m^2+m), where m = len(i)
        if self.get(value):
            i = self.hash(value)
            for j in self.slots[i]:
                if j == value:
                    self.slots[i].remove(value)
                    self.count -= 1
                    return True
        return False

    def intersection(self, set2):
        # O(n^2*m), where n = len(set) and m = len(i)
        res = PowerSet()
        for i in range(len(set2.slots)):
            for val in set2.slots[i]:
                if self.get(val):
                    res.put(val)
        return res

    def union(self, set2):
        # O(n^2*m), where n = len(set) and m = len(i)
        for i in range(len(set2.slots)):
            for val in set2.slots[i]:
                self.put(val)
        return self 

    def difference(self, set2):
        # O(n^2*m), where n = len(set) and m = len(i)
        res = PowerSet()
        for i in range(len(self.slots)):
            for val in self.slots[i]:
                if not set2.get(val):
                    res.put(val)
        return res

    def issubset(self, set2):
        # O(n^2*m), where n = len(set) and m = len(i)
        count = 0
        length = 0
        for i in range(len(set2.slots)):
            for val in set2.slots[i]:
                if self.get(val):
                    count += 1
            length += len(set2.slots[i])
        if count == length:
            return True
        return False
