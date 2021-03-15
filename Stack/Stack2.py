# https://skillsmart.ru/algo/py-kf32y/f1f7e6c832b.html

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def pop(self):
        if self.size():
            itm = self.stack[0]
            del self.stack[0]
            return itm
        return None

    def push(self, value):
        self.stack.insert(0, value)
    
    def peek(self):
        if self.size():
            return self.stack[0]
        return None

    '''
    Использование динамических массивов повышает сложность алгоритма, это может возникнуть за счет реаллокации при переполнении массива.
    Поэтому стоит использовать в качестве базовой структуры данных в стеках - связанный список.
    Функции pop() и push() в выше приведенном коде имеют ассимптоту O(n) (каждая). А в связанных списках эта сложность равна у каждой по O(1).
    См. реализацию стека с динамическим массивом в stack1.py.
    '''
