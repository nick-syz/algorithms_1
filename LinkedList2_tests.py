from LinkedList2 import Node, LinkedList2

def print_all_nodes(lst):
    node = lst.head
    while node is not None:
        print(node.value)
        node = node.next

def test_1():
    lst = LinkedList2()
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(4))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    print_all_nodes(lst)
    lst.delete(1, all=True)
    print('---')
    print_all_nodes(lst)
    assert lst.len() == 3

def test_2():
    lst = LinkedList2()
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(4))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    print_all_nodes(lst)
    lst.delete(1)
    print('---')
    print_all_nodes(lst)
    assert lst.len() == 8

def test_3():
    lst = LinkedList2()
    n3 = Node(3)
    n10 = Node(10)
    lst.add_in_tail(n10)
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(n3)
    lst.add_in_tail(Node(4))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(1))
    print_all_nodes(lst)
    print('---')
    n5 = Node(5)
    lst.insert(n3, n5)
    print(f'next5={n5.next.value}')
    print(f'prev5={n5.prev.value}')
    n50 = Node(50)
    lst.insert(n10, n50)
    print(f'next={n50.next.value}')
    print(f'prev={n50.prev.value}')
    n100 = Node(100)
    lst.insert(None, n100)
    print(f'n100next={n100.next.value}')
    print(f'n100prev={n100.prev}')
    print_all_nodes(lst)

def test_4():
    lst = LinkedList2()
    for i in range(5):
        lst.add_in_tail(Node(i))
    lst.insert(None, Node(10))
    print_all_nodes(lst)

def test_5():
    lst = LinkedList2()
    for i in range(5):
        lst.add_in_tail(Node(i))
    n10 = Node(10)
    lst.add_in_tail(n10)
    lst.insert(n10, Node(999))
    print_all_nodes(lst)

if __name__ == '__main__':
    test_5()
