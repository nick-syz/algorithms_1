from Stack import Stack

def Balanced(brackets):
    if not len(brackets):
        return False
    stack = Stack()
    for i in brackets:
        if stack.size():
            if i == '(':
                stack.push(i)
            elif stack.peek() == '(':
                stack.pop()
        else:
            stack.push(i)
    if not stack.size():
        return True
    return False
