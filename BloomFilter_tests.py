from BloomFilter import BloomFilter
from unittest import TestCase

class BloomFilterTest(TestCase):
    def setUp(self):
        self.s1 = '1234567890'
        self.s2 = '2345678901'
        self.s3 = '3456789012'
        self.s4 = '4567890123'
        self.s5 = '5678901234'
        self.s6 = '6789012345'
        self.s7 = '7890123456'
        self.s8 = '8901234567'
        self.s9 = '9012345678'
        self.s10 = '0123456789'
        
        self.bloom = BloomFilter(10)
        self.zero = BloomFilter(0)

    def test_add(self):
        self.assertEqual(False, self.bloom.is_value(self.s1))
        self.assertEqual(False, self.bloom.is_value(self.s2))
        self.assertEqual(False, self.bloom.is_value(self.s3))
        self.assertEqual(False, self.bloom.is_value(self.s4))
        self.assertEqual(False, self.bloom.is_value(self.s5))
        self.assertEqual(False, self.bloom.is_value(self.s6))
        self.assertEqual(False, self.bloom.is_value(self.s7))
        self.assertEqual(False, self.bloom.is_value(self.s8))
        self.assertEqual(False, self.bloom.is_value(self.s9))
        self.assertEqual(False, self.bloom.is_value(self.s10))

        self.bloom.add(self.s1)
        self.assertEqual(True, self.bloom.is_value(self.s1))

        self.bloom.add(self.s2)
        self.bloom.add(self.s3)
        self.bloom.add(self.s4)
        self.bloom.add(self.s5)
        self.bloom.add(self.s6)
        self.bloom.add(self.s7)
        self.bloom.add(self.s8)
        
        # self.assertEqual(False, self.bloom.is_value('8901234567'))
        # self.assertEqual(False, self.bloom.is_value('9012345678'))
        # self.assertEqual(False, self.bloom.is_value('0123456789'))

        self.bloom.add(self.s9)
        self.bloom.add(self.s10)

    def test_empty(self):
        self.zero.add(self.s1)

        self.assertEqual(0, self.zero.filter_len)
        self.assertEqual(0, self.zero.mask)
        
        self.assertEqual(False, self.zero.is_value(self.s1))
        self.assertEqual(False, self.zero.is_value(self.s2))
        self.assertEqual(False, self.zero.is_value(self.s3))
        self.assertEqual(False, self.zero.is_value(self.s4))
        self.assertEqual(False, self.zero.is_value(self.s5))
        self.assertEqual(False, self.zero.is_value(self.s6))
        self.assertEqual(False, self.zero.is_value(self.s7))
        self.assertEqual(False, self.zero.is_value(self.s8))
        self.assertEqual(False, self.zero.is_value(self.s9))
        self.assertEqual(False, self.zero.is_value(self.s10))
