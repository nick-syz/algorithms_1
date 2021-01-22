# https://skillsmart.ru/algo/py-kf32y/a92175914c12.html

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class _DummyNode(Node):
    def __init__(self):
        super().__init__(None)

class OrderedList:
    def __init__(self, asc):
        self.head = _DummyNode()
        self.tail = _DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.__ascending = asc
        self.length = 0

    def compare(self, v1, v2):
        if v1 >= v2:
            return True
        return False

    def add(self, value):
        new_node = Node(value)
        if not self.length:
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node
        else:    
            node = self.head.next
            while node is not self.tail:
                # checking current value
                more = self.compare(new_node.value, node.value)
                # checking next value
                less = None
                if node.next.value is None:
                    if self.__ascending:
                        less = True
                    else:
                        less = False
                else:
                    less = self.compare(node.next.value, new_node.value)
                # adding new value
                if more and less and self.__ascending or not more and not less and not self.__ascending:
                    new_node.next = node.next
                    new_node.prev = node
                    node.next.prev = new_node
                    node.next = new_node
                    break
                elif not more and self.__ascending or more and not self.__ascending:
                    new_node.next = node
                    new_node.prev = node.prev
                    node.prev.next = new_node
                    node.prev = new_node
                    break
                node = node.next
        self.length += 1

    def find(self, val):
        head = self.head.next.value
        tail = self.tail.prev.value
        if val == head:
            return self.head.next
        elif val == tail:
            return self.tail.prev
        elif val > head and val < tail or val < head and val > tail:
            node = self.head.next
            while node is not self.tail:
                if val == node.value:
                    return node
                node = node.next
        return None

    def delete(self, val):
        if self.length:
            node = self.find(val)
            if node:
                self.length -= 1
                node.prev.next, node.next.prev = node.next, node.prev

    def clean(self, asc):
        self.length = 0
        self.__ascending = asc
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        return self.length

    def get_all(self):
        r = []
        node = self.head.next
        while node is not self.tail:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() >= v2.strip():
            return True
        return False
