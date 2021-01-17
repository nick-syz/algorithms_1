from Stack import Stack

def Balanced(brackets):
    if not len(brackets):
        return False
    stack = Stack()
    for i in brackets:
        if stack.size():
            if stack.peek() == '(' and i == ')':
                stack.pop()
            else:
                stack.push('(')
        elif not stack.size():
            stack.push(i)
    if not stack.size():
        return True
    return False
