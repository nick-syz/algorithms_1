from Brackets import Balanced
from unittest import TestCase

class Brackets_test(TestCase):
    def test(self):
        self.assertEqual(False, Balanced(''))
        self.assertEqual(False, Balanced('('))
        self.assertEqual(False, Balanced(')'))
        self.assertEqual(False, Balanced('))'))
        self.assertEqual(False, Balanced(')('))
        self.assertEqual(False, Balanced('(('))
        self.assertEqual(True, Balanced('()'))
        self.assertEqual(False, Balanced('())'))
        self.assertEqual(False, Balanced('))()))'))
        self.assertEqual(False, Balanced('(()'))
        self.assertEqual(True, Balanced('((()))'))
        self.assertEqual(False, Balanced('(()))))'))
        self.assertEqual(False, Balanced('(((((('))
        self.assertEqual(False, Balanced(')))))))'))
        self.assertEqual(False, Balanced('(((((('))
        self.assertEqual(False, Balanced(')))(((('))
        self.assertEqual(False, Balanced(')))((('))
