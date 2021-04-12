from HashTable import HashTable
from unittest import TestCase

class HashTableTest(TestCase):
    def setUp(self):
        self.table = HashTable(11, 3)

    def test_put1(self):
        self.table.put('Mia')
        self.table.put('Tim')
        self.table.put('Bea')
        self.table.put('Zoe')

        r = [v for v in self.table.slots]
        self.assertEqual(['Bea', 'Tim', None, None, 'Mia', 'Zoe', None, None, None, None, None], r)

        self.table.put('Sue')
        r = [v for v in self.table.slots]
        self.assertEqual(['Bea', 'Tim', None, None, 'Mia', 'Zoe', 'Sue', None, None, None, None], r)

        self.table.put('Len')
        r = [v for v in self.table.slots]
        self.assertEqual(['Bea', 'Tim', None, 'Len', 'Mia', 'Zoe', 'Sue', None, None, None, None], r)

        self.table.put('Moe')
        r = [v for v in self.table.slots]
        self.assertEqual(['Bea', 'Tim', None, 'Len', 'Mia', 'Zoe', 'Sue', 'Moe', None, None, None], r)

        self.table.put('Lou')
        r = [v for v in self.table.slots]
        self.assertEqual(['Bea', 'Tim', None, 'Len', 'Mia', 'Zoe', 'Sue', 'Moe', None, 'Lou', None], r)

        self.table.put('Rae')
        r = [v for v in self.table.slots]
        self.assertEqual(['Bea', 'Tim', None, 'Len', 'Mia', 'Zoe', 'Sue', 'Moe', None, 'Lou', 'Rae'], r)

        self.table.put('Max')
        r = [v for v in self.table.slots]
        self.assertEqual(['Bea', 'Tim', None, 'Len', 'Mia', 'Zoe', 'Sue', 'Moe', 'Max', 'Lou', 'Rae'], r)

        #self.table.put('Tod')
        #r = [v for v in self.table.slots]
        #self.assertEqual(['Bea', 'Tim', 'Tod', 'Len', 'Mia', 'Zoe', 'Sue', 'Moe', 'Max', 'Lou', 'Rae'], r)

    def test_put2(self):
        self.table = HashTable(17, 15)
        self.table.put('Bea')
        self.table.put('Tim')
        self.table.put('Tod')
        self.table.put('Len')
        self.table.put('Mia')
        self.table.put('Zoe')
        self.table.put('Sue')
        self.table.put('Moe')
        self.table.put('Max')
        self.table.put('Tod')
        self.table.put('Lou')
        self.table.put('Rae')

        r = [v for v in self.table.slots if v != None]
        self.assertEqual(len(r), 12)
