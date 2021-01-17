from Queue2 import Queue
from unittest import TestCase

class Queue2Test(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.assertEqual(0, self.queue.size()) # length(queue) = 0
        self.queue.enqueue(1) # 1
        self.queue.enqueue(2) # 1 <- 2
        self.queue.enqueue(3) # 1 <- 2 <- 3

        self.assertEqual(3, self.queue.size()) # length(queue) = 3
        self.assertEqual(0, self.queue.top) # top_index = 0
        self.assertEqual(1, self.queue.array.__getitem__(0)) # top_value = 1
        
        for i in range(4, 17):
            self.queue.enqueue(i) # 1 <- 2 <- 3 <- 4 <- 5 <- .. <- 16

        self.assertEqual(16, self.queue.size()) # length(queue) = 16
        self.assertEqual(16, self.queue.array.capacity) # capacity(array) = 16

    def test_dequeue(self):
        self.assertEqual(0, self.queue.size()) # length(queue) = 0
        self.queue.enqueue(1) # 1
        self.queue.enqueue(2) # 1 <- 2
        self.queue.enqueue(3) # 1 <- 2 <- 3

        self.assertEqual(3, self.queue.size()) # length(queue) = 3

        self.assertEqual(1, self.queue.dequeue()) # 2 <- 3
        self.assertEqual(3, self.queue.array.__len__()) # length(array) = 3
        
        self.assertEqual(1, self.queue.top) # top_index = 1
        self.assertEqual(2, self.queue.array.__getitem__(self.queue.top)) # top_value = 2

        for i in range(4, 17):
            self.queue.enqueue(i) # 2 <- 3 <- 4 <- 5 <- .. <- 16

        self.assertEqual(15, self.queue.size()) # length(queue) = 15
        self.assertEqual(2, self.queue.dequeue()) # 3 <- .. <- 17
        self.assertEqual(16, self.queue.array.__getitem__(15))
        # self.assertEqual(17, self.queue.array.__getitem__(16))

