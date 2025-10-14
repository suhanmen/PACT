def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) >= 2 and stack[-2] == '[':
                return True
            stack.pop()
    return False
