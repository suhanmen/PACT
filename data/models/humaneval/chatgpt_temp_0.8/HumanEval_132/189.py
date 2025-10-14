def is_nested(string):
    stack = []
    for char in string:
        if char == "[":
            stack.append(char)
        elif char == "]" and len(stack) > 0:
            stack.pop()
            if len(stack) > 0:
                return True
    return False
