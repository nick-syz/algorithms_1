from Queue1 import Queue
from unittest import TestCase

class QueueTest(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test(self):
        self.assertEqual(0, self.queue.size()) # length(queue) = 0
        self.queue.enqueue(1) # 1
        self.queue.enqueue(2) # 1 <- 2
        self.queue.enqueue(3) # 1 <- 2 <- 3
        self.queue.enqueue(4) # 1 <- 2 <- 3 <- 4

        self.assertEqual(4, self.queue.size()) # length(queue) = 0

        self.assertEqual(1, self.queue.dequeue()) # 2 <- 3 <- 4
        self.assertEqual(2, self.queue.dequeue()) # 3 <- 4
        self.assertEqual(3, self.queue.dequeue()) # 4
        self.assertEqual(4, self.queue.dequeue()) # empty

        self.assertEqual(None, self.queue.dequeue()) # Queue is an empty
