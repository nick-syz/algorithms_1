class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
                if node.next is not None and node.prev is not None:
                    node.prev.next, node.next.prev = node.next, node.prev
                elif node.next == None:
                    self.tail = node.prev
                    node.prev.next = node.next
                elif node.prev == None:
                    self.head = node.next
                    node.next.prev = None
                if not all:
                    return
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
        node = self.head
        if afterNode is None:
            if node == None:
                newNode.next, node.prev = node, newNode
                newNode.prev = None
                self.head = newNode
            else:
                self.tail.next, newNode.prev = newNode, self.tail
                newNode.next = None
                self.tail = newNode
            return
        while node is not None:
            if node == afterNode:
                if afterNode.next != None:
                    afterNode.next, newNode.next = newNode, node.next
                    newNode.prev, node.prev = afterNode, newNode
                else:
                    afterNode.next, newNode.next = newNode, None
                    newNode.prev = afterNode
                    self.tail = newNode
                return
            node = node.next

    def add_in_head(self, newNode):
        node = self.head
        if node:
            newNode.next, node.prev = node, newNode
        else:
            newNode.next = None
        self.head = newNode
        
