# https://skillsmart.ru/algo/py-kf32y/f1f7e6c832b.html

class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def size(self):
        return self.count
    
    def pop(self):
        if self.count:
            self.count -= 1
            return self.stack[self.count]
        return None

    def push(self, value):
        if self.count < len(self.stack):
            self.stack[self.count] = value
        else:
            self.stack.append(value)
        self.count += 1

    def peek(self):
        if self.count:
            return self.stack[0]
        return None

    '''
    Вариант реализации стека: верхние элементы в конце массива, нижние - в начале.
    Данный вариант лучше, чем реализация в Stack.py. Но проблема с реаллокацией никуда не делась. При переполнении массива сложность возрастет до O(n).
    '''
