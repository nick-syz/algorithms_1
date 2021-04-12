from NativeCache import NativeCache
from unittest import TestCase

class NativeCacheTest(TestCase):
    def setUp(self):
        self.cache = NativeCache(11)

    def test_add_in_free_cache(self):
        for i in range(11):
            self.cache.put(str(i), str(i))

        for i in range(11):
            self.assertEqual(str(i), self.cache.get(str(i)))

        for i in range(11, 20):
            self.assertIsNone(self.cache.get(str(i)))

    def test_add_in_full_cache(self):
        self.assertEqual(0, self.cache.elements_count)
        for i in range(11):
            self.cache.put(str(i), str(i))
        self.assertEqual(11, self.cache.elements_count)

        self.cache.put('11', '11')
        for i in range(5):
            self.assertEqual('11', self.cache.get('11'))
        i = self.cache.hits.index(6)
        self.assertEqual('11', self.cache.keys[i])

        self.cache.put('12', '12')
        self.assertEqual('12', self.cache.get('12'))
        self.assertEqual('11', self.cache.get('11'))

        self.cache.put('21', '21')
        self.assertEqual('21', self.cache.get('21'))
        self.assertEqual('12', self.cache.get('12'))
        
        for i in range(11):
            self.cache.get(str(i))
        
    def test_collisions(self):
        for i in range(11):
            self.cache.put(str(i), str(i))
        
        self.cache.put('12', '12')
        self.cache.put('21', '21')
        self.assertEqual(None, self.cache.get('12'))
        
        self.assertEqual('10', self.cache.get('10'))
        
        self.cache.put('01', '01')
        self.assertEqual('10', self.cache.get('10'))
        self.assertEqual('01', self.cache.get('01'))
