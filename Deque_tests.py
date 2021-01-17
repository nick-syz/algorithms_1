from Deque import Deque
from unittest import TestCase

class DequeTest(TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_removeFront(self):
        self.assertEqual(0, self.deque.size()) # length(deque) = 0
        self.deque.addFront(1) # 1
        self.deque.addFront(2) # 2 <- 1
        self.deque.addFront(3) # 3 <- 2 <- 1

        self.assertEqual(3, self.deque.size()) # length(deque) = 3

        self.assertEqual(3, self.deque.removeFront()) # 2 <- 1
        self.assertEqual(2, self.deque.size()) # length(deque) = 2

        self.assertEqual(2, self.deque.removeFront()) # 1
        self.assertEqual(1, self.deque.removeFront()) # Empty

        self.assertEqual(0, self.deque.size()) # length(deque) = 0
        self.assertEqual(None, self.deque.removeFront()) # Deque is an empty

    def test_removeTail(self):
        self.assertEqual(0, self.deque.size()) # length(deque) = 0
        self.deque.addTail(1) # 1
        self.deque.addTail(2) # 2 <- 1
        self.deque.addTail(3) # 3 <- 2 <- 1

        self.assertEqual(3, self.deque.size()) # length(deque) = 3

        self.assertEqual(3, self.deque.removeTail()) # 3 <- 2
        self.assertEqual(2, self.deque.removeTail()) # 3
        self.assertEqual(1, self.deque.removeTail()) # Empty

        self.assertEqual(0, self.deque.size()) # length(deque) = 0
        self.assertEqual(None, self.deque.removeTail()) # Deque is an empty

    def test1(self):
        self.deque.addFront(1) # 1
        self.deque.addTail(2) # 1 <-> 2
        self.deque.addFront(3) # 3 <- 1 <-> 2
        self.deque.addTail(4) # 3 <- 1 <-> 2 -> 4
        self.deque.addTail(6) # 3 <- 1 <-> 2 -> 4 -> 6

        self.assertEqual(5, self.deque.size()) # length(deque) = 5

        self.assertEqual(3, self.deque.removeFront()) # 1 <-> 2 -> 4 -> 6
        self.assertEqual(6, self.deque.removeTail()) # 1 <-> 2 -> 4
        self.assertEqual(1, self.deque.removeFront()) # 2 -> 4

        self.assertEqual(2, self.deque.removeFront()) # 4
        self.assertEqual(4, self.deque.removeTail()) # Empty

        self.assertEqual(None, self.deque.removeFront())
        self.assertEqual(None, self.deque.removeTail())
