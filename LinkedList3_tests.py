from LinkedList3 import LinkedList3, Node
from unittest import TestCase

class LinkedList3Test(TestCase):

    def setUp(self):
        self.list = LinkedList3()

    def test_add_in_tail(self):
        n1 = Node(1)
        self.list.add_in_tail(n1)
        self.assertEqual(self.list.head.next, n1)
        self.assertEqual(self.list.tail.prev, n1)

    def test_find(self):
        n2 = Node(2)
        n3 = Node(3)
        self.list.add_in_tail(n2)
        self.list.add_in_tail(n3)
        
        # check first element in the list
        self.assertEqual(self.list.head.next, n2)
         
        # check len list
        self.assertEqual(2, self.list.len())

        # check what element is found
        self.assertEqual(n2, self.list.find(2))

        # check wrong element
        self.assertEqual(None, self.list.find(22))

    def test_find_all(self):
        self.list.clean()
        self.assertEqual(0, self.list.len())
        
        n2_1 = Node(2)
        n2_2 = Node(2)
        self.list.add_in_tail(n2_1)
        self.list.add_in_tail(n2_2)

        # check list len
        self.assertEqual(2, self.list.len())

        # check find all
        self.assertEqual([n2_1, n2_2], self.list.find_all(2))

    def test_delete(self):
        self.assertEqual(0, self.list.len())
        
        lst = [Node(1), Node(1), Node(5), Node(6), Node(1), Node(1), Node(8), Node(1), Node(1)]
        for i in lst:
            self.list.add_in_tail(i)
        
        self.assertEqual(9, self.list.len())

        # check delete with few elements
        # check all=False
        self.list.delete(1)
        self.assertEqual(8, self.list.len())
        self.assertEqual(lst[1], self.list.head.next)

        # check all=True
        self.list.delete(1, all=True)
        self.assertEqual(3, self.list.len())
        self.assertEqual(self.list.head.next, lst[2])
        self.assertEqual(self.list.tail.prev, lst[-3])

        self.list.delete(5)
        self.list.delete(6)
        self.assertEqual(1, self.list.len())

        self.list.delete(8)
        self.assertEqual(0, self.list.len())

    def test_insert(self):
        self.assertEqual(0, self.list.len())
        
        # test insert afterNode=None in empty list
        n55 = Node(55)
        self.list.insert(None, n55)
        self.assertEqual(1, self.list.len())

        # test insert afterNode=None in not empty list
        n44 = Node(44)
        self.list.insert(None, n44)
        self.assertEqual(self.list.tail.prev, n44)
        self.assertEqual(n44.prev, n55)
        self.assertEqual(2, self.list.len())
        self.assertEqual(n44.next, self.list.tail)

        # test insert right afterNode in not empty list
        n66 = Node(66)
        self.list.insert(n44, n66)
        self.assertEqual(3, self.list.len())

        # test insert not right afterNode in empty list
        self.list.insert(Node(12), Node(55))
        self.assertEqual(3, self.list.len())

        # test insert afterNode!=None in empty list
        self.list.clean()
        self.assertEqual(0, self.list.len())

        self.list.insert(Node(1), Node(5))
        self.assertEqual(0, self.list.len())

    def test_add_in_head(self):
        n23 = Node(23)
        self.list.add_in_tail(n23)
        
        n34 = Node(34)
        self.list.add_in_head(n34)
        self.assertEqual(self.list.head.next, n34)

        self.assertEqual(n34.prev, self.list.head)
        self.assertEqual(n34.next, n23)

        self.assertEqual(n23.prev, n34)
