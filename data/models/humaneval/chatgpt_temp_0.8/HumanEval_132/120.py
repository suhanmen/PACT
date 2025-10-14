def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']' and stack:
            stack.pop()
        elif bracket == ']' and not stack:
            return False
    return len(stack) != len(string)
