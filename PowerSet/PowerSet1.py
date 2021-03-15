class PowerSet:

    def __init__(self):
        self.slots = list()

    def size(self):
        return len(self.slots)

    def put(self, value):
        if not value in self.slots:
            self.slots.append(value)

    def get(self, value):
        if value in self.slots:
            return True
        return False

    def remove(self, value):
        if value in self.slots:
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):
        res = PowerSet()
        for i in self.slots:
            if i in set2.slots:
                res.put(i)
        return res 

    def union(self, set2):
        res = PowerSet()
        res.slots = self.slots
        for i in set2.slots:
            res.put(i)
        return res

    def difference(self, set2):
        res = PowerSet()
        for i in self.slots:
            if not i in set2.slots:
                res.put(i)
        return res

    def issubset(self, set2):
        for i in set2:
            if not i in self.slots:
                return False
        return True
