from LinkedList2 import Node, LinkedList2
from unittest import TestCase

class LinkedList2Test(TestCase):

    def setUp(self):
        self.list = LinkedList2()

    def test_find(self):
        # test with empty list
        self.assertEqual(None, self.list.find(1))
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

        # test with one element in the list
        n1 = Node(1)
        self.list.add_in_tail(n1)
        self.assertEqual(n1, self.list.find(1))
        self.assertEqual(None, self.list.find(2))
        self.assertEqual(n1, self.list.head)
        self.assertEqual(n1, self.list.tail)

        # test with few elements in the list
        self.list.clean()
        lst = [Node(2), Node(2), Node(3), Node(3)]
        for i in lst:
            self.list.add_in_tail(i)    
        
        self.assertEqual(None, self.list.find(5))
        self.assertEqual(lst[0], self.list.find(2))
        self.assertEqual(lst[2], self.list.find(3))
    
    def test_find_all(self):
        
        # test with null elements in the list
        self.list.clean()
        self.assertEqual([], self.list.find_all(2))
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

        # test with one element in the list
        n1 = Node(1)
        self.list.add_in_tail(n1)
        self.assertEqual([self.list.find(1)], self.list.find_all(1))
        self.assertEqual(n1, self.list.head)
        self.assertEqual(n1, self.list.tail)

        # test with few elements in the list
        lst = [Node(2), Node(2), Node(3), Node(3)]
        for i in lst:
            self.list.add_in_tail(i)

        self.assertEqual([lst[0], lst[1]], self.list.find_all(2))
        self.assertEqual(n1, self.list.head)
        self.assertEqual(lst[3], self.list.tail)

    def test_delete(self):
        
        # test with null elements in the list
        self.list.clean()
        self.list.delete(1)
        self.assertEqual(0, self.list.len())
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

        # test with one element in the list
        n1 = Node(1)
        self.list.add_in_tail(n1)
        self.list.delete(5)
        self.assertEqual(1, self.list.len())
        self.assertEqual(n1, self.list.head)
        self.assertEqual(n1, self.list.tail)

        self.list.delete(1)
        self.assertEqual(0, self.list.len())
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

        # test with few elements in the list
        lst = [Node(1), Node(1), Node(5), Node(1), Node(1), Node(4), Node(6), Node(1), Node(1)]
        for i in lst:
            self.list.add_in_tail(i)

        self.list.delete(1)
        self.assertEqual(len(lst)-1, self.list.len())
        self.assertEqual(lst[1], self.list.head)
        self.assertEqual(lst[-1], self.list.tail)
        
        self.list.delete(1, all=True)
        self.assertEqual(3, self.list.len())
        self.assertEqual(lst[2], self.list.head)

        n5 = self.list.find(5)
        self.assertEqual(n5.prev, None)
        self.assertEqual(n5.next, lst[-4])

        self.assertEqual(lst[-3], self.list.tail)

        n6 = self.list.find(6)
        self.assertEqual(n6.prev, lst[-4])
        self.assertEqual(n6.next, None)
        
        # test - delete last element
        self.list.clean()
        n22 = Node(22)
        self.list.add_in_tail(n22)
        self.list.delete(22)
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)

    def test_insert(self):
        # ----- test with null elements in the list
        self.list.clean()
        n99 = Node(99)
        
        # afterNode = None in empty list
        self.list.insert(None, n99)
        self.assertEqual(n99, self.list.head)
        self.assertEqual(n99, self.list.tail)

        # afterNode != None in empty list
        n44 = Node(44)
        
        # insert after wrong node
        self.list.insert(n44, Node(33))
        self.assertEqual(1, self.list.len())

        # insert after right node
        n32 = Node(32)
        self.list.insert(n99, n32)
        self.assertEqual(2, self.list.len())
        self.assertEqual(n99, self.list.head)
        self.assertEqual(n32, self.list.tail)

        #----- test with one element
        self.list.clean()
        n123 = Node(123)
        self.list.add_in_tail(n123)

        # afterNode == None in one element list
        n321 = Node(321)
        self.list.insert(None, n321)
        self.assertEqual(n123, self.list.head)
        self.assertEqual(n321, self.list.tail)

        # afterNode != None
        n55 = Node(55)
        self.list.insert(n321, n55)
        self.assertEqual(n55, self.list.tail)
        self.assertEqual(n123, self.list.head)
        n55_obj = self.list.find(55)
        self.assertEqual(n55_obj.prev, n321)
        
        #----- test with few elements
        n66 = Node(66)
        self.list.insert(n55, n66)
        self.assertEqual(n66, self.list.tail)
        self.assertEqual(n55.next, n66)
        n66_obj = self.list.find(66)
        self.assertEqual(n66_obj.prev, n55)
    
    def test_in_head(self):
        # test with null element in the list
        self.list.clean()
        n1 = Node(1)
        self.list.add_in_head(n1)

        self.assertEqual(n1, self.list.head)
        self.assertEqual(n1, self.list.tail)
        n1_obj = self.list.find(1)
        self.assertEqual(n1_obj.prev, None)
        self.assertEqual(n1_obj.next, None)

        # test with one element in the list
        n22 = Node(22)
        self.list.add_in_head(n22)
        
        self.assertEqual(n22, self.list.head)
        self.assertEqual(n1, self.list.tail)
