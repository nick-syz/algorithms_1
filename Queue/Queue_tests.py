from Queue import Queue
from unittest import TestCase

class QueueTest(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.assertEqual(0, self.queue.size()) # size(queue) = 0
        self.queue.enqueue(1) # queue -> 1
        self.assertEqual(1, self.queue.size()) # size(queue) = 1
    
    def test_dequeue(self):
        self.assertEqual(None, self.queue.dequeue()) # queue is an empty
        self.assertEqual(0, self.queue.size()) # size(queue) = 0
        self.queue.enqueue(1) # queue -> 1
        self.queue.enqueue(2) # queue -> 1 -> 2
        self.queue.enqueue(3) # queue -> 1 -> 2 -> 3
        
        self.assertEqual(1, self.queue.head.next.value)
        self.assertEqual(2, self.queue.head.next.next.value)
        self.assertEqual(1, self.queue.head.next.next.prev.value)
        self.assertEqual(3, self.queue.tail.prev.value)
        self.assertEqual(2, self.queue.tail.prev.prev.value)
        self.assertEqual(self.queue.tail, self.queue.tail.prev.next)
        self.assertEqual(self.queue.head, self.queue.head.next.prev)

        self.assertEqual(3, self.queue.size()) # size(queue) = 3

        self.assertEqual(1, self.queue.dequeue()) # queue -> 2 -> 3
        self.assertEqual(2, self.queue.dequeue()) # queue -> 3
        self.assertEqual(3, self.queue.dequeue()) # queue -> empty
        
        self.assertEqual(0, self.queue.size()) # size(queue) = 0
        
        self.assertEqual(None, self.queue.dequeue()) # None
