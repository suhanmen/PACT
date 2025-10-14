def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if stack:
                stack.pop()
            else:
                return False
        if len(stack) > 1:
            return True
    return False
