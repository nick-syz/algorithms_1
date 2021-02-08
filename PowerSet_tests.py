from PowerSet import PowerSet
from unittest import TestCase

class PowerSetTest(TestCase):
    def setUp(self):
        self.set = PowerSet()
        self.set2 = PowerSet()
        self.l = 20000
    '''
    def test_get(self):
        for i in range(20000):
            self.set.put(str(i))
        
        for i in range(20000):
            self.set.put(str(i))

        for i in range(20000):
            self.assertEqual(True, self.set.get(str(i)))
    '''
    def test_remove(self):
        for i in range(self.l):
            self.set.put(str(i))

        for i in range(self.l):
            self.assertEqual(True, self.set.get(str(i)))

        self.assertEqual(self.l, self.set.size())

        for i in range(self.l):
            self.assertEqual(True, self.set.remove(str(i)))
        
        self.assertEqual(0, self.set.size())

    def test_intersection(self):
        
        for i in range(self.l):
            self.set2.put(str(i))

        for i in range(self.l):
            self.set.put(str(i))

        self.assertEqual(self.l, self.set2.size())

        res = self.set.intersection(self.set2)
        self.assertEqual(self.l, res.size())
        
    def test_union(self):
        for i in range(self.l, 2*self.l):
            self.set2.put(str(i))

        for i in range(self.l):
            self.set.put(str(i)) 

        res = self.set.union(self.set2)

        self.assertEqual(2*self.l, res.size())

    def test_difference(self):
        for i in range(self.l):
            self.set.put(str(i))

        for i in range(self.l):
            self.set2.put(str(i))
        
        res = self.set.difference(self.set2)

        self.assertEqual(0, res.size())

    def test_difference1(self):
        for i in range(self.l): 
            self.set.put(str(i))

        for i in range(self.l, 2*self.l):
            self.set2.put(str(i))

        res = self.set.difference(self.set2)

        self.assertEqual(self.l, self.set.size())

    def test_issubset(self):
        for i in range(self.l):
            self.set.put(str(i))

        for i in range(self.l):
            self.set2.put(str(i))

        res = self.set.issubset(self.set2)

        self.assertEqual(True, res)
