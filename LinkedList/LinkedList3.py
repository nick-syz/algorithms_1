# https://skillsmart.ru/algo/py-kf32y/y6a342a5104u.html

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class _DummyNode(Node):
    def __init__(self):
        super().__init__(None)

class LinkedList3:
    def __init__(self):
        self.head = _DummyNode()
        self.tail = _DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def add_in_tail(self, item):
        item.prev, item.next = self.tail.prev, self.tail
        self.tail.prev.next = item
        self.tail.prev = item
        self.length += 1

    def find(self, val):
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = list()
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes
    
    def delete(self, val, all=False):
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                node.prev.next, node.next.prev = node.next, node.prev
                self.length -= 1
                if not all:
                    break
            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def len(self):
        return self.length
    
    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head.next is self.tail:
                self.head.next = newNode
                newNode.prev = self.head
            else:
                newNode.prev = self.tail.prev
                self.tail.prev.next = newNode
            newNode.next = self.tail
            self.tail.prev = newNode
            self.length += 1
        else:
            if self.head.next is not self.tail:
                newNode.next = afterNode.next
                afterNode.next, newNode.prev = newNode, afterNode
                self.length += 1

    def add_in_head(self, newNode):
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.length += 1
