from OrderedList import OrderedList, OrderedStringList
from unittest import TestCase

class OrderedListTest(TestCase):
    def setUp(self):
        self.list = OrderedList(True)
        self.list1 = OrderedStringList(True)
    
    def test_add1(self):
        self.assertEqual(0, self.list.len()) # length(list) = 0
        self.list.add(22) # 22
        self.list.add(2) # 2 -> 22
        self.list.add(1) # 1 -> 2 -> 22
        self.list.add(6) # 1 -> 2 -> 6 -> 22
        self.list.add(10) # 1 -> 2 -> 6 -> 10 -> 22
        self.list.add(3) # 1 -> 2 -> 3 -> 6 -> 10 -> 22
        self.list.add(8) # 1 -> 2 -> 3 -> 6 -> 8 -> 10 -> 22
        self.list.add(1) # 1 -> 1 -> 2 -> 3 -> 6 -> 8 -> 10 -> 22
        self.assertEqual(8, self.list.len()) # length(list) = 7
        self.assertEqual(1, self.list.head.next.value)
        
        r = [node.value for node in self.list.get_all() if node.value != None]
        self.assertEqual([1, 1, 2, 3, 6, 8, 10, 22], r)

    def test_add2(self):
        self.list = OrderedList(False)

        self.assertEqual(0, self.list.len()) # length(list) = 0
        self.list.add(33) # 33
        self.list.add(1) # 33 -> 1
        self.list.add(6) # 33 -> 6 -> 1
        self.list.add(10) # 33 -> 10 -> 6 -> 1
        self.list.add(3) # 33 -> 10 -> 6 -> 3 -> 1
        self.list.add(10) # 33 -> 10 -> 10 -> 6 -> 3 -> 1
        self.list.add(8) # 33 -> 10 -> 10 -> 8 -> 6 -> 3 -> 1
        self.assertEqual(7, self.list.len()) # length(list) = 7
        self.assertEqual(33, self.list.head.next.value)
        
        r = [node.value for node in self.list.get_all() if node.value != None]
        self.assertEqual([33, 10, 10, 8, 6, 3, 1], r)

    def test_find(self):
        self.list = OrderedList(False)

        self.assertEqual(0, self.list.len()) # length(list) = 0
        self.list.add(33) # 33
        self.list.add(1) # 33 -> 1
        self.list.add(6) # 33 -> 6 -> 1
        self.list.add(10) # 33 -> 10 -> 6 -> 1
        self.list.add(3) # 33 -> 10 -> 6 -> 3 -> 1
        self.list.add(10) # 33 -> 10 -> 10 -> 6 -> 3 -> 1
        self.list.add(8) # 33 -> 10 -> 10 -> 8 -> 6 -> 3 -> 1
        self.assertEqual(7, self.list.len()) # length(list) = 7
        self.assertEqual(33, self.list.head.next.value)
        
        node = self.list.find(10)
        self.assertEqual(10, node.value)

        node = self.list.find(100)
        self.assertEqual(None, node)

        node = self.list.find(33)
        self.assertEqual(33, node.value)

    def test_delete(self):
        self.assertEqual(0, self.list.len())
        
        self.list.delete(5)
        self.assertEqual(0, self.list.len())

        self.list.add(22) # 22
        self.list.add(2) # 2 -> 22
        self.list.add(1) # 1 -> 2 -> 22
        self.list.add(6) # 1 -> 2 -> 6 -> 22
        self.list.add(10) # 1 -> 2 -> 6 -> 10 -> 22
        self.list.add(3) # 1 -> 2 -> 3 -> 6 -> 10 -> 22
        self.list.add(8) # 1 -> 2 -> 3 -> 6 -> 8 -> 10 -> 22
        self.list.add(1) # 1 -> 1 -> 2 -> 3 -> 6 -> 8 -> 10 -> 22
        
        self.assertEqual(8, self.list.len()) # length(list) = 7
        self.assertEqual(1, self.list.head.next.value)

        self.list.delete(22)
        r = [node.value for node in self.list.get_all() if node.value != None]
        self.assertEqual([1, 1, 2, 3, 6, 8, 10], r)
        self.assertEqual(7, self.list.len())

        self.list.delete(1)
        r = [node.value for node in self.list.get_all() if node.value != None]
        self.assertEqual([1, 2, 3, 6, 8, 10], r)
        self.assertEqual(6, self.list.len())

        self.list.delete(5)
        r = [node.value for node in self.list.get_all() if node.value != None]
        self.assertEqual([1, 2, 3, 6, 8, 10], r)
        self.assertEqual(6, self.list.len())

        self.list.delete(6)
        r = [node.value for node in self.list.get_all() if node.value != None]
        self.assertEqual([1, 2, 3, 8, 10], r)
        self.assertEqual(5, self.list.len())

        self.list.delete(1)
        self.list.delete(2)
        self.list.delete(3)
        self.list.delete(8)
        self.list.delete(10)

        self.assertEqual(0, self.list.len())
    
    def test_string_add(self):
        self.list1.add('a') # 'a'
        self.list1.add('r') # 'a' -> 'r'
        self.list1.add('e') # 'a' -> 'e' -> 'r'

        self.assertEqual(3, self.list1.len())
        
        r = [node.value for node in self.list1.get_all() if node.value != None]
        self.assertEqual(['a', 'e', 'r'], r)
     
    def test_string_add1(self):
        self.list1.clean(False) # empty list
        self.list1.add('e ') # 'e'
        self.list1.add('  e') # 'e' -> 'e'
        self.list1.add('a ') # 'e' -> 'e' -> 'a'
        self.list1.add('   z') # 'z' -> 'e' -> 'e' -> 'a'
        self.list1.add('k ') # 'z' -> 'k' -> 'e' -> 'e' -> 'a'
        self.list1.add(' k') # 'z' -> 'k' -> 'k' -> 'e' -> 'e' -> 'a'
        self.assertEqual(6, self.list1.len())
        
        r = [node.value for node in self.list1.get_all() if node.value != None]
        self.assertEqual(['   z', ' k', 'k ', '  e', 'e ', 'a '], r)
