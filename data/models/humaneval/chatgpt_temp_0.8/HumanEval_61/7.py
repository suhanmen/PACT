def correct_bracketing(brackets: str):
    stack = []
    for b in brackets:
        if b == '(':
            stack.append('(')
        elif b == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
