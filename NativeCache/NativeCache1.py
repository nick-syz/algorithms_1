# https://skillsmart.ru/algo/py-kf32y/z1467b2a4244.html

class Node:
    def __init__(self, key, val, i):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None
        self.index = i

class _DummyNode(Node):
    def __init__(self):
        super(_DummyNode, self).__init__(None, None)

class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.head = _DummyNode()
        self.tail = _DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def hash_fun(self, key):
        return sum(key.encode()) % self.size

    def add_in_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def put(self, key, value):
        i = self.hash_fun(key)
        if self.count == self.size:
            if self.count <= 1:
                self.head.next = self.prev
                sef.tail.prev = self.head
            else:
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
            self.count -= 1
        else:
            step = 3
            node = Node(key, value)
            while step < self.size:
                if self.slots[i] is None:
                    self.slots[i] = key
                    self.values[i] = value
                    self.add_in_head(node)
                    self.count += 1
                    break
                i += step-1
                if i > self.size-1:
                    i = abs(i-self.size-1)
                    step += 1
    
    def get(self, key):
        node = self.head.next
        while node is not self.tail:
            if node.key == key:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.add_in_head(node)
                return node.value
            node = node.next
        return None
