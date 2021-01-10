from LinkedList import Node, LinkedList

def test_1():
    lst = LinkedList()
    lst.add_in_tail(Node(10))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(5))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.delete(1, all=True)
    lst.print_all_nodes()
    print('---')
    print(f'head={lst.head.value} next={lst.head.next.value}')
    print(f'tail={lst.tail.value} next={lst.tail.next}')
    assert lst.len() == 5

def test_2():
    lst = LinkedList()
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(10))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(5))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(5))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.delete(1)
    lst.print_all_nodes()
    assert lst.len() == 11

def test_3():
    lst = LinkedList()
    lst.add_in_tail(Node(10))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(5))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.clean()
    print(f'head={lst.head}')
    print(f'tail={lst.tail}')
    lst.print_all_nodes()
    assert lst.len() == 0

def test_4():
    lst = LinkedList()
    lst.add_in_tail(Node(10))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(4))
    lst.add_in_tail(Node(5))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(1))
    lst.insert(Node(1), Node(2))
    lst.insert(None, Node(100))
    lst.print_all_nodes()
    print('---')
    print(f'head={lst.head.value} next={lst.head.next.value}')
    print(f'tail={lst.tail.value} next={lst.tail.next}')

def sum_lists(list_1, list_2):
    if list_1.len() == list_2.len():
        node1 = list_1.head
        node2 = list_2.head
        while node1 != None and node2 != None:
            node1.value = node1.value + node2.value
            node1 = node1.next
            node2 = node2.next
        return list_1

def test_5():
    lst1 = LinkedList()
    lst2 = LinkedList()
    lst1.add_in_tail(Node(10))
    lst1.add_in_tail(Node(22))
    lst2.add_in_tail(Node(1))
    lst2.add_in_tail(Node(2))
    lst = sum_lists(lst1, lst2)
    lst.print_all_nodes()

def test_6():
    lst = LinkedList()
    assert lst.len() == 0

def test_7():
    lst = LinkedList()
    lst.insert(Node(1), Node(2))
    lst.print_all_nodes()
    print(lst.len())
    lst.delete(1)
    lst.print_all_nodes()
    print(lst.find_all(1))
    print(lst.find(1))

def test_8():
    lst = LinkedList()
    lst.add_in_tail(Node(1))
    print(lst.head.value)
    print(lst.tail.next)

def test_9():
    lst = LinkedList()
    n10 = Node(10)
    for i in range(5):
        lst.add_in_tail(Node(i))
    lst.add_in_tail(n10)
    lst.insert(n10, Node(99))
    lst.print_all_nodes()

if __name__ == '__main__':
    test_9()
