from Stack import Stack

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.length = 0

    def enqueue(self, item):
        self.stack1.push(item)
        self.length += 1

    def dequeue(self):
        self.length -= 1
        while self.stack1.size():
            self.stack2.push(self.stack1.pop())
        if self.stack2.size():
            return self.stack2.pop()
        return None
    
    def size(self):
        return self.length
