from Stack import Stack
from unittest import TestCase

class Stack_test(TestCase):
    
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.size())
        
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(4, self.stack.size())

    def test_pop(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.size())

        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(4, self.stack.size())

        self.assertEqual(4, self.stack.pop())
        self.assertEqual(3, self.stack.pop())

        self.assertEqual(2, self.stack.size())
        
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())

        self.assertEqual(0, self.stack.size())

        self.assertEqual(None, self.stack.pop())

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(3, self.stack.peek())
        self.stack.pop()
        self.assertEqual(2, self.stack.peek())

        self.stack.pop()
        self.stack.pop()
        self.assertEqual(None, self.stack.peek())


