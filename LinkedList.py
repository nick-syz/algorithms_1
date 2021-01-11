# https://skillsmart.ru/algo/py-kf32y/fb50h6802e1s.html

class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = list()
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if self.head != node and self.tail != node:
                    node_prev.next = node.next
                    node = node_prev
                elif self.tail == node:
                    self.tail = node_prev
                    node_prev.next = node.next
                elif self.head == node:
                    self.head = node.next
                if not all:
                    return
            node_prev = node
            node = node.next
    
    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        n = 0
        node = self.head
        while node is not None:
            n += 1
            node = node.next
        return n

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.head, newNode.next = newNode, self.head
        else:
            if self.head is not None:
                if self.tail == afterNode:
                    self.tail = newNode
                afterNode.next, newNode.next = newNode, afterNode.next
