def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0 or stack[-1] != '[':
                continue
            stack.pop()
            if len(stack) > 0:
                return True
    return False
