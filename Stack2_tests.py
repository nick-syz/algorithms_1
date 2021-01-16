from Stack2 import Stack
from unittest import TestCase

class Stack2_test(TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(0, self.stack.size()) # length(stack) = 0
        self.stack.push(1) # stack -> 1 (top)
        
        self.assertEqual(1, self.stack.size()) # length(stack) = 1

        self.stack.push(2) # stack -> 2 (top) -> 1
        self.stack.push(3) # stack -> 3 (top) -> 2 -> 1

        self.assertEqual(3, self.stack.size()) # length(stack) = 3

        self.assertEqual(3, self.stack.head.next.value) # top = 3

    def test_pop(self):
        self.stack.push(1) # stack -> 1 (top)
        self.stack.push(2) # stack -> 2 (top) -> 1
        self.stack.push(3) # stack -> 3 (top) -> 2 -> 1

        self.assertEqual(3, self.stack.size()) # length(stack) = 3

        self.assertEqual(3, self.stack.pop()) # old_top = 3, stack -> 2 (top), 1
        self.assertEqual(2, self.stack.size()) # length = 2

        self.assertEqual(2, self.stack.head.next.value) # top = 2

        self.assertEqual(2, self.stack.pop()) # old_top = 2, stack -> 1 (top)
        self.assertEqual(1, self.stack.size()) # length(stack) = 1
        self.assertEqual(1, self.stack.head.next.value) # top = 1

        self.assertEqual(1, self.stack.pop()) # old_top = 1, stack -> None
        self.assertEqual(0, self.stack.size()) # lenght(stack) = 0

        self.assertEqual(self.stack.tail, self.stack.head.next) # stack is an  empty

        self.assertEqual(None, self.stack.pop()) # None top
    
    def test_seek(self):
        self.stack.push(3) # stack -> 3 (top)
        self.stack.push(2) # stack -> 2 (top) -> 3
        self.stack.push(1) # stack -> 1 (top) -> 2 -> 3

        self.assertEqual(1, self.stack.peek()) # peek = 1

        self.assertEqual(1, self.stack.pop()) # old_top = 1, stack -> 2 (top) -> 3

        self.assertEqual(2, self.stack.peek()) # peek = 2
        self.stack.pop() # stack -> 3 (top)
        self.assertEqual(3, self.stack.pop()) # old_top = 3, stack -> empty
        self.assertEqual(None, self.stack.pop()) # stack is an empty

        self.assertEqual(None, self.stack.peek()) # peek = None
