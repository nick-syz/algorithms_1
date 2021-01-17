from Stack import Stack

def S1_gen(string):
    S1 = Stack()
    for i in string[::-1]:
        if i is not ' ':
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
        elif i is '+':
            S2.push(S2.pop()+S2.pop())
        elif i is '*':
            S2.push(S2.pop()*S2.pop())
        elif i is '=':
            return S2.peek()
    raise 'Please, add "=" in the end of your expression.'
