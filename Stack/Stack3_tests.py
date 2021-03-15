from Stack3 import Stack
from unittest import TestCase

class Stack3Test(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(0, self.stack.size()) # length(stack) = 0
        
        self.stack.push(1) # 1
        self.stack.push(2) # 2 <- 1
        self.stack.push(3) # 3 <- 2 <- 1

        self.assertEqual(3, self.stack.size()) # length(stack) = 3

    def test_pop(self):
        self.assertEqual(0, self.stack.size()) # length(stack) = 0
        
        self.stack.push(1) # 1
        self.stack.push(2) # 2 <- 1
        self.stack.push(3) # 3 <- 2 <- 1
        self.stack.push(4) # 4 <- 3 <- 2 <- 1

        self.assertEqual(4, self.stack.pop()) # 3 <- 2 <- 1
        self.assertEqual(3, self.stack.size()) # length(stack) = 3

        self.assertEqual(3, self.stack.pop()) # 2 <- 1
        self.assertEqual(2, self.stack.pop()) # 1
        self.assertEqual(1, self.stack.pop()) # empty

        self.assertEqual(None, self.stack.pop()) # stack is an empty
