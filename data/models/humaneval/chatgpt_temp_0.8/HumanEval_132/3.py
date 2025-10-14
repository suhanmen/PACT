def is_nested(string):
    stack = []
    for char in string:
        if char == "[":
            stack.append(char)
        elif char == "]":
            if not stack:
                return False
            stack.pop()
            if not stack:
                return True
    return False
