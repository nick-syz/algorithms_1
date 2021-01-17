from Palindrom import palindrom
from unittest import TestCase

class PalindromTest(TestCase):

    def test(self):
        self.assertEqual(True, palindrom('шалаш'))
        self.assertEqual(True, palindrom('xxxx'))
        self.assertEqual(False, palindrom('xt'))
        self.assertEqual(False, palindrom('yxxxyy'))
        self.assertEqual(True, palindrom('x'))
        self.assertEqual(False, palindrom('werwer'))
        self.assertEqual(True, palindrom('ppoiwerrewiopp'))
        # iself.assertEqual(False, palindrom(''))
