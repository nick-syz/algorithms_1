# https://skillsmart.ru/algo/py-kf32y/o744d98d29c3.html

import ctypes

class DynArray:

    def __init__(self):
        self.elements_count = 0
        self.array_capacity = 16
        self.array = self.make_array(self.array_capacity)

    def __len__(self):
        return self.elements_count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, index):
        if index < 0 or index >= self.elements_count:
            raise IndexError('Index is out of bounds')
        return self.array[index]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.elements_count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.array_capacity = new_capacity

    def append(self, added_item):
        if self.elements_count == self.array_capacity:
            self.resize(2*self.array_capacity)
        self.array[self.elements_count] = added_item
        self.elements_count += 1

    def insert(self, index_of_inserted_item, inserted_item):
        if index_of_inserted_item < 0 or index_of_inserted_item > self.elements_count:
            raise IndexError('Index is out of bounds')
        if self.elements_count == self.array_capacity:
            self.resize(2*self.array_capacity)
        self.elements_count += 1
        if index_of_inserted_item == self.elements_count-1:
            self.array[index_of_inserted_item] = inserted_item
        else:
            previosly_item = None
            for some_index in range(self.elements_count):
                if some_index > index_of_inserted_item:
                    if some_index < self.elements_count-1:
                        self.array[some_index], previosly_item = \
                                previosly_item, self.array[some_index]
                    else:
                        self.array[some_index] = previosly_item
                elif some_index == index_of_inserted_item:
                    previosly_item = self.array[some_index]
                    self.array[some_index] = inserted_item

    def delete(self, index_of_deleted_item):
        if index_of_deleted_item < 0 or index_of_deleted_item >= self.elements_count:
            raise IndexError('Index is out of bounds')
        for some_index in range(self.elements_count):
            if some_index > index_of_deleted_item:
                self.array[some_index-1] = self.array[some_index]
        self.elements_count -= 1
        if self.elements_count < self.array_capacity*0.5:
            if int(self.array_capacity/1.5) < 16:
                self.resize(16)
            else:
                self.resize(int(self.array_capacity/1.5))
