from PowerSet import PowerSet
from unittest import TestCase

class PowerSetTest(TestCase):

    def setUp(self):
        self.set = PowerSet()
        self.set2 = PowerSet()

    def test_difference1(self):
        # set is empty and set2 is empty
        self.assertEqual(0, (self.set.difference(self.set2)).size())
        self.assertEqual(0, (self.set2.difference(self.set)).size())
    
    def test_difference2(self):
        # set is not empty and set2 is empty
        self.set.put('1') # set {1}
        # set-set2 = {1} - {} = {1}
        res = self.set.difference(self.set2)
        self.assertEqual(1, res.size()) # -> {1}
        self.assertEqual(True, res.get('1'))
    
    def test_difference3(self):
        # set is empty and set2 is not empty
        self.set2.put('2') # set2 {2}
        # set {}
        # set-set2 = {} - {2} = {}
        res = self.set.difference(self.set2)
        self.assertEqual(0, res.size()) # -> {}
        self.assertEqual(False, res.get('1'))
    
    def test_difference4(self):
        # set is not empty and set2 is not empty
        self.assertEqual(0, self.set.size())
        self.assertEqual(0, self.set.size())
        self.set.put('1') # set {1}
        self.set.put('2') # set {1, 2}
        self.set2.put('3') # set2 {3}
        self.set2.put('2') # set2 {2, 3}
        # set-set2 = {1, 2} - {2, 3} = {1}
        res = self.set.difference(self.set2)
        self.assertEqual(True, res.get('1'))
        self.assertEqual(False, res.get('2'))
        self.assertEqual(1, res.size()) # -> {1}
