def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) > 0 and stack[-1] == '[':
                return True
            stack.pop()
    return False
