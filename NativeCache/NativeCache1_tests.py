from NativeCache1 import NativeCache
from unittest import TestCase

class NativeCacheTest(TestCase):
    def setUp(self):
        self.cache = NativeCache(11)

    def test_put(self):
        for i in range(11):
            self.cache.put(str(i), str(i))

        self.assertEqual(11, self.cache.count)

    def test_get(self):
        for i in range(11):
            self.cache.put(str(i), str(i))

        self.assertEqual(self.cache.size, self.cache.count)
        self.cache.put('11', '11')
        print(self.cache.slots)
         
        self.assertEqual('11', self.cache.get('11'))
