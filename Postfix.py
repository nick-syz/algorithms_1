from Stack2 import Stack

def S1_gen(string):
    S1 = Stack()
    for i in string[::-1]:
        if i != ' ':
            S1.push(i)
    return S1

def calculate(string):
    if not len(string):
        return None
    S1 = S1_gen(string)
    S2 = Stack()
    while S1.size():
        i = S1.pop()
        if i.isnumeric():
            S2.push(int(i))
        elif i in '+*=':
            num = 0
            if i == '+':
                while S2.size():
                    num += S2.pop()
            elif i == '*':
                num = 1
                while S2.size():
                    num *= S2.pop()
            elif i == '=':
                return S2.peek()
            S2.push(num)
    return 'Please, add "=" in the end of your expression.'
