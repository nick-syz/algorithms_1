from BloomFilter import BloomFilter
from unittest import TestCase

class BloomFilterTest(TestCase):
    def setUp(self):
        self.bloom = BloomFilter(10)

    def test_add(self):
        self.assertEqual(0, self.bloom.arr[0])
        self.bloom.add('0123456789')
        self.assertEqual(1, self.bloom.arr[-1])
        self.assertEqual(True, self.bloom.is_value('0123456789'))

        self.bloom.add('1234567890')
        self.bloom.add('2345678901')
        self.bloom.add('3456789012')
        self.bloom.add('4567890123')
        self.bloom.add('5678901234')
        self.bloom.add('6789012345')
        self.bloom.add('7890123456')
        
        # self.assertEqual(False, self.bloom.is_value('8901234567'))
        # self.assertEqual(False, self.bloom.is_value('9012345678'))
        # self.assertEqual(False, self.bloom.is_value('0123456789'))

        self.bloom.add('8901234567')
        self.bloom.add('9012345678')
        self.bloom.add('0123456789')
