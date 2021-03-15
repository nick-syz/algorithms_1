from Queue import Queue
from QueueCycle import Cycle
from unittest import TestCase

class QueueCycle_test(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test(self):
        self.queue.enqueue(1) #  1
        self.queue.enqueue(2) #  1 <- 2
        self.queue.enqueue(3) #  1 <- 2 <- 3
        self.queue.enqueue(4) #  1 <- 2 <- 3 <- 4
 
        self.assertEqual(4, self.queue.size()) # length(enqueue) = 4
        
        self.queue = Cycle(1, self.queue) # 2 <- 3 <- 4 <- 1
        
        self.assertEqual(2, self.queue.head.next.value) # head = 2
        self.assertEqual(1, self.queue.tail.prev.value) # tail = 1

        self.queue = Cycle(3, self.queue) # 1 <- 2 <- 3 <- 4

        self.assertEqual(1, self.queue.head.next.value) # head = 1
        self.assertEqual(4, self.queue.tail.prev.value) # tail = 4
