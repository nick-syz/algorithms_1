from Deque import Deque

def palindrom(string):
    if not len(string):
        raise 'String is an empty!'
    deque = Deque()
    count = 0
    for i in range(len(string)//2):
        deque.addFront(string[i])
        deque.addTail(string[-(i+1)])
        if deque.removeFront() == deque.removeTail():
            count += 1
    if count == len(string)//2:
        return True
    return False
