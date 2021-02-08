from PowerSet import PowerSet
from unittest import TestCase

class PowerSetTest(TestCase):
    def setUp(self):
        self.set = PowerSet()
        self.set2 = PowerSet()
        self.l = 20000

    def test_get(self):
        for i in range(20000):
            self.set.put(str(i))
        
        for i in range(20000):
            self.set.put(str(i))

        for i in range(20000):
            self.assertEqual(True, self.set.get(str(i)))

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

        # set = full and set2 = full
        res = self.set.intersection(self.set2)
        self.assertEqual(self.l, res.size())
        
        # set = full and set2 = empty
        res1 = self.set.intersection(PowerSet())
        self.assertEqual(0, res1.size())

        # set = empty and set2 = full
        res2 = PowerSet().intersection(self.set2)
        self.assertEqual(0, res2.size())

        # set = empty and set2 = empty
        res3 = PowerSet().intersection(PowerSet())
        self.assertEqual(0, res3.size())

    def test_union(self):
        for i in range(self.l, 2*self.l):
            self.set2.put(str(i))

        for i in range(self.l):
            self.set.put(str(i)) 

        # set = full and set2 = full
        res = self.set.union(self.set2)
        self.assertEqual(2*self.l, res.size())
        
        # set = full and set2 = empty
        res1 = self.set.union(PowerSet())
        self.assertEqual(self.l, res1.size())

        # set = empty and set2 = full
        res2 = PowerSet().union(self.set2)
        self.assertEqual(self.l, res2.size())

        # set = empty and set2 = empty
        res3 = PowerSet().union(PowerSet())
        self.assertEqual(0, res3.size())

    def test_difference(self):
        for i in range(self.l):
            self.set.put(str(i))

        for i in range(self.l):
            self.set2.put(str(i))
        
        # set = full and set2 = full
        res = self.set.difference(self.set2)
        self.assertEqual(0, res.size())

        # set = full and set2 = empty
        res1 = self.set.difference(PowerSet())
        self.assertEqual(self.l, res1.size())

        # set = empty and set2 = full
        res2 = PowerSet().difference(self.set2)
        self.assertEqual(0, res2.size())

        # set = empty and set2 = empty
        res3 = PowerSet().difference(PowerSet())
        self.assertEqual(0, res3.size())

    def test_difference1(self):
        for i in range(self.l): 
            self.set.put(str(i))

        for i in range(self.l, 2*self.l):
            self.set2.put(str(i))
        
    def test_issubset(self):
        for i in range(self.l):
            self.set.put(str(i))

        for i in range(self.l):
            self.set2.put(str(i))
         
        # set = full and set2 = full
        res = self.set.issubset(self.set2)
        self.assertEqual(True, res)

        # set = full and set2 = empty
        res1 = self.set.issubset(PowerSet())
        self.assertEqual(False, res1)
        
        # set = empty and set2 = full
        res2 = PowerSet().issubset(self.set2)
        self.assertEqual(False, res2)

        # set = empty and set2 = empty
        res3 = PowerSet().issubset(PowerSet())
        self.assertEqual(True, res3)

    def test_issubset1(self):
        for i in range(self.l):
            self.set.put(str(i))

        for i in range(self.l-4):
            self.set2.put(str(i))

        res = self.set.issubset(self.set2)
        self.assertEqual(False, res)
    
        res1 = self.set2.issubset(self.set)
        self.assertEqual(False, res1)
