from PowerSet1 import PowerSet
from unittest import TestCase

class PowerSetTest(TestCase):
    def setUp(self):
        self.set = PowerSet()

    def test_get(self):
        for i in range(20000):
            self.set.put(str(i))

        for j in range(20000):
            self.assertEqual(True, self.set.get(str(j)))
