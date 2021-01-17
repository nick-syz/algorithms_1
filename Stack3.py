from Queue import Queue

'''
The stack realization by two queues.
push() - O(1);
pop() - O(n).
'''

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.length = 0 

    def push(self, val):
        self.q1.enqueue(val)
        self.length += 1

    def pop(self):
        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())
        if self.q1.size:
            val = self.q1.dequeue()
            self.q1, self.q2 = self.q2, self.q1
            self.length -= 1
            return val
        return None

    def size(self):
        return self.length
