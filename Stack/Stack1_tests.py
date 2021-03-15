from Stack1 import Stack
from unittest import TestCase

class Stack1_test(TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(0, len(self.stack.stack))
        self.stack.push(1) # stack -> 1 (top)
        self.assertEqual(1, self.stack.size()) # size(stack) = 1

        self.stack.push(2) # stack -> 2 (top) -> 1
        self.assertEqual(2, self.stack.size()) # size(stack) = 2

    def test_pop(self):
        self.stack.push(1) # stack -> 1 (top)
        self.stack.push(2) # stack -> 2 (top) -> 1
        self.stack.push(3) # stack -> 3 (top) -> 2 -> 1

        self.assertEqual(3, self.stack.pop()) # old_top = 3, stack -> 2 (top) -> 1
        self.assertEqual(2, self.stack.pop()) # old_top = 2, stack -> 1 (top)
        self.assertEqual(1, self.stack.pop()) # old_top = 1, stack is empty
        self.assertEqual(None, self.stack.pop()) # stack is an empty
        
        self.assertEqual(0, self.stack.size())
