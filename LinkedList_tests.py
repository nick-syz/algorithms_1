from LinkedList import Node, LinkedList
from unittest import TestCase

class LinkedListTest(TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_find_all(self):
        n1 = Node(1)
        n1_1 = Node(1)
        n2 = Node(2)
        n5 = Node(5)
        
        self.list.add_in_tail(n1)
        self.list.add_in_tail(n2)
        self.list.add_in_tail(n1_1)
        self.list.add_in_tail(n5)

        # verify len list
        self.assertEqual(4, self.list.len())

        # verify finding all elements
        self.assertEqual([n1, n1_1], self.list.find_all(n1.value))

        # verify finding elements in empty list
        self.assertEqual(None, self.list.find_all(LinkedList()))
        
        # vertify finding 1 element
        self.lst = LinkedList()
        n22 = Node(22)
        self.lst.add_in_tail(n22)
        self.assertEqual([n22], self.lst.find_all(n22.value))
    
    def test_delete(self):
        self.list.clean()
        n1 = Node(1)
        n1_2 = Node(1)
        n1_3 = Node(1)
        n2 = Node(2)
        n5 = Node(5)
        n1_4 = Node(1)
        n1_5 = Node(1)
        n1_6 = Node(1)

        self.list.add_in_tail(n1)
        self.list.add_in_tail(n1_2)
        self.list.add_in_tail(n1_3)
        self.list.add_in_tail(n2)
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(n5)
        self.list.add_in_tail(n1_4)
        self.list.add_in_tail(n1_5)
        self.list.add_in_tail(n1_6)

        # check len list
        self.assertEqual(9, self.list.len())

        # check delete, all=False
        self.list.delete(1)
        self.assertEqual(8, self.list.len())

        # check delete, all=True
        self.list.delete(1, all=True)
        self.assertEqual(2, self.list.len())

        # check head
        head = self.list.head
        self.assertEqual(head, self.list.find(n2.value))

        # check tail
        tail = self.list.tail
        self.assertEqual(tail, self.list.find(n5.value))

    def test_insert(self):
        self.list.clean()

        n1 = Node(1)
        n1_1 = Node(1)
        n2 = Node(2)
        n5 = Node(5)

        self.list.add_in_tail(n1)
        self.list.add_in_tail(n2)
        self.list.add_in_tail(n1_1)
        self.list.add_in_tail(n5)

        # check list len
        self.assertEqual(4, self.list.len())

        # check insert
        n55 = Node(55)
        self.list.insert(n1, n55)
        self.assertEqual(n55, self.list.find(n55.value))
        n55_obj = self.list.find(n55.value)
        self.assertEqual(n55, n1.next)
        
        # check head
        self.assertEqual(n1, self.list.head)

        # check tail
        self.assertEqual(n5, self.list.tail)

        # check insert None
        n111 = Node(111)
        self.list.insert(None, n111)
        
        # check head
        self.assertEqual(n111, self.list.head)

        # check tail
        self.assertEqual(n5, self.list.tail)

        # check next
        n111_obj = self.list.find(n111.value)
        self.assertEqual(n1, n111_obj.next)

    def test_empty(self):
        self.list = LinkedList()
        n55 = Node(55)
        self.list.insert(None, n55)
        self.assertEqual(self.list.head, self.list.find(n55.value))

        self.list.clean()

        self.list.insert(Node(1), Node(55))
        self.assertEqual(None, self.list.head)
        self.assertEqual(None, self.list.tail)
