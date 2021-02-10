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
            self.set.put(str(i)) # -> {0..99}

        for i in range(100, 200):
            self.set2.put(str(i)) # -> {100..199}
        
        # {0..99} - {100..199} = {0..99}
        res = self.set.difference(self.set2)

        # {100..199} - {0..99} = {100..199}
        res1 = self.set2.difference(self.set)

        self.assertEqual(100, res.size())
        self.assertEqual(100, res1.size())
        
        for i in range(100):
            self.assertEqual(True, res.get(str(i)))

        for i in range(100, 200):
            self.assertEqual(True, res1.get(str(i)))


    def test_difference2(self):
        for i in range(100):
            self.set.put(str(i)) # -> {0..99}

        for i in range(50, 150):
            self.set2.put(str(i)) # -> {50..149}
        
        # {0..99} - {50..149} = {0..49}
        res = self.set.difference(self.set2)

        # {50..149} - {0..99} = {100..149}
        res1 = self.set2.difference(self.set)

        self.assertEqual(50, res.size())
        self.assertEqual(50, res1.size())

        for i in range(50):
            self.assertEqual(True, res.get(str(i)))

        for i in range(100, 150):
            self.assertEqual(True, res1.get(str(i)))
    
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
