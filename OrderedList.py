# https://skillsmart.ru/algo/py-kf32y/a92175914c12.html

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.length = 0

    def compare(self, v1, v2):
        if v1 >= v2:
            return True
        return False

    def add(self, value):
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:    
            node = self.head
            while node is not None:
                # checking current value
                more = self.compare(new_node.value, node.value)
                # checking next value
                less = None
                if node.next is None:
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
                    if node.next is not None:
                        node.next.prev = new_node
                    node.next = new_node
                    if node is self.tail:
                        self.tail = new_node
                    break
                elif not more and self.__ascending or more and not self.__ascending:
                    new_node.next = node
                    new_node.prev = node.prev
                    if node.prev is not None:
                        node.prev.next = new_node
                    node.prev = new_node
                    if node is self.head:
                        self.head = new_node
                    break
                node = node.next
        self.length += 1

    def find(self, val):
        head = self.head.value
        tail = self.tail.value
        if val == head:
            return self.head
        elif val == tail:
            return self.tail
        elif val > head and val < tail or val < head and val > tail:
            node = self.head
            while node is not None:
                if val == node.value:
                    return node
                node = node.next
        return None

    def delete(self, val):
        if self.length:
            node = self.find(val)
            if node:
                self.length -= 1
                if node is self.head and node is self.tail:
                    self.head = None
                    self.tail = None
                elif node is not self.head and node is not self.tail:
                    node.prev.next, node.next.prev = node.next, node.prev
                elif node is self.tail:
                    self.tail, node.prev.next = node.prev, node.next
                elif node is self.head:
                    self.head, node.next.prev = node.next, node.prev

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.length = 0

    def len(self):
        return self.length

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
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
