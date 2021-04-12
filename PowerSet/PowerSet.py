# https://skillsmart.ru/algo/py-kf32y/s83e6f8ef537.html

class PowerSet:

    def __init__(self):
        self.set_size = 373
        self.slots = [[] for i in range(self.set_size)]
        self.elements_count = 0

    def hash(self, value):
        return sum(value.encode()) % self.set_size
    
    def size(self):
        return self.elements_count

    def put(self, value):
        hash_index = self.hash(value)
        if value not in self.slots[hash_index]:
            self.slots[hash_index].append(value)
            self.elements_count += 1

    def get(self, value):
        hash_index = self.hash(value)
        if value in self.slots[hash_index]: 
            return True
        return False

    def remove(self, removed_value):
        hash_index = self.hash(removed_value)
        if self.elements_count:
            for value in self.slots[hash_index]:
                if value == removed_value:
                    self.slots[hash_index].remove(removed_value)
                    self.elements_count -= 1
                    return True
        return False

    def intersection(self, set2):
        result_of_intersection = PowerSet()
        for i in range(len(set2.slots)):
            for value_from_set2 in set2.slots[i]:
                if self.get(value_from_set2):
                    result_of_intersection.put(value_from_set2)
        return result_of_intersection

    def union(self, set2):
        result_of_union = PowerSet()
        for i in range(len(self.slots)):
            for value_from_set1 in self.slots[i]:
                result_of_union.put(value_from_set1)
        for i in range(len(set2.slots)):
            for value_from_set2 in set2.slots[i]:
                result_of_union.put(value_from_set2)
        return result_of_union

    def difference(self, set2):
        result_of_difference = PowerSet()
        for i in range(len(self.slots)):
            for value_from_set1 in self.slots[i]:
                if not set2.get(value_from_set1):
                    result_of_difference.put(value_from_set1)
        return result_of_difference

    def issubset(self, set2):
        for i in range(len(set2.slots)):
            for val in set2.slots[i]:
                if not self.get(val):
                    return False
        return True
