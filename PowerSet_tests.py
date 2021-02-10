from PowerSet import PowerSet
from unittest import TestCase

class PowerSetTest(TestCase):
    def setUp(self):
        self.set = PowerSet()
        self.set2 = PowerSet()

    def test_get(self):
        for i in range(100):
            self.set.put(str(i)) # -> {0..99}
        
        for i in range(100):
            self.assertEqual(True, self.set.get(str(i)))
        
        self.assertEqual(100, self.set.size()) # size({0..99}) = 100   

    def test_remove(self):
        for i in range(100):
            self.set.put(str(i)) # -> {0..99}

        for i in range(100):
            self.assertEqual(True, self.set.get(str(i)))

        for i in range(100, 200):
            self.assertEqual(False, self.set.get(str(i)))
        
        for i in range(100):
            self.set.remove(str(i)) # -> {}

        self.assertEqual(0, self.set.size()) # size({}) = 0

    def test_intersection(self):
        for i in range(100):
            self.set2.put(str(i)) # -> set2 = {0..99}

        for i in range(100):
            self.set.put(str(i)) # -> set = {0..99}

        self.assertEqual(100, self.set2.size())

        # set = full and set2 = full
        res = self.set.intersection(self.set2)
        self.assertEqual(100, res.size())
        
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
        for i in range(100, 200):
            self.set2.put(str(i)) # set2 = {100..199}

        for i in range(100):
            self.set.put(str(i)) # set = {0..99}

        # set = full and set2 = full
        res = self.set.union(self.set2)
        self.assertEqual(200, res.size())
        
        # set = full and set2 = empty
        res1 = self.set.union(PowerSet())
        self.assertEqual(100, res1.size())

        # set = empty and set2 = full
        res2 = PowerSet().union(self.set2)
        self.assertEqual(100, res2.size())

        # set = empty and set2 = empty
        res3 = PowerSet().union(PowerSet())
        self.assertEqual(0, res3.size())

    def test_difference(self):
        for i in range(100):
            self.set.put(str(i))

        for i in range(100):
            self.set2.put(str(i))
        
        # set = full and set2 = full
        res = self.set.difference(self.set2)
        self.assertEqual(0, res.size())

        # set = full and set2 = empty
        res1 = self.set.difference(PowerSet())
        self.assertEqual(100, res1.size())

        # set = empty and set2 = full
        res2 = PowerSet().difference(self.set2)
        self.assertEqual(0, res2.size())

        # set = empty and set2 = empty
        res3 = PowerSet().difference(PowerSet())
        self.assertEqual(0, res3.size())

    def test_difference1(self):
        for i in range(100): 
            self.set.put(str(i))

        for i in range(100, 200):
            self.set2.put(str(i))
        
        self.assertEqual(100, (self.set.difference(self.set2).size()))
        self.assertEqual(100, (self.set2.difference(self.set).size()))

    def test_difference2(self):
        self.set.put(str(1))
        self.set.put(str(2))
        self.set.put(str(3)) # set = {1, 2, 3}

        self.set2.put(str(5))
        self.set2.put(str(20))
        self.set2.put(str(10))
        self.set2.put(str(4)) # set2 = {5, 20, 10, 4}

        self.assertEqual(3, (self.set.difference(self.set2)).size()) # {1, 2, 3}
        self.assertEqual(True, self.set.get(str(1)))
        self.assertEqual(True, self.set.get(str(2)))
        self.assertEqual(True, self.set.get(str(3)))

        self.set2.put(str(1))
        self.set2.put(str(2))
        self.set2.put(str(3)) # set2 = {5, 20, 10, 4, 1, 2, 3}

        self.assertEqual(0, (self.set.difference(self.set2).size())) # {}

        self.assertEqual(4, (self.set2.difference(self.set).size())) # {5, 20, 10, 4}

    def test_issubset(self):
        for i in range(100):
            self.set.put(str(i))

        for i in range(100):
            self.set2.put(str(i))
         
        # set = full and set2 = full
        res = self.set.issubset(self.set2)
        self.assertEqual(True, res)

        # set = full and set2 = empty
        res1 = self.set.issubset(PowerSet())
        self.assertEqual(True, res1)
        
        # set = empty and set2 = full
        res2 = PowerSet().issubset(self.set2)
        self.assertEqual(False, res2)

        # set = empty and set2 = empty
        res3 = PowerSet().issubset(PowerSet())
        self.assertEqual(True, res3)
    
    def test_issubset1(self):
        for i in range(100):
            self.set.put(str(i))

        for j in range(56):
            self.set2.put(str(j))

        self.assertEqual(True, self.set.issubset(self.set2))
        
        # len(set2) < len(set)
        self.assertEqual(False, self.set2.issubset(self.set))
