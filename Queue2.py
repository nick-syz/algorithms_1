from DynArray import DynArray

'''
The Queue realizaiton by array with fixed length.
enqueue() - O(1);
dequeue() - O(1).
'''

class Queue:
    def __init__(self):
        self.array = DynArray()
        self.top = 0
        self.length = 0

    def enqueue(self, itm):
        if self.array.count >= self.array.capacity:
            raise 'Error! Array is a full.'
        self.array.append(itm)
        self.length += 1

    def dequeue(self):
        if self.length:
            self.top += 1
            self.length -= 1
            return self.array.__getitem__(self.top-1)
        return None
        
    def size(self):
        return self.length
