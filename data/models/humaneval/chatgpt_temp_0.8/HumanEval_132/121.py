def is_nested(string):
    stack = []
    nested = False
    for char in string:
        if char == "[":
            stack.append(char)
        elif char == "]":
            if len(stack) > 0:
                stack.pop()
                nested = True
        if len(stack) == 0 and nested:
            return True
    return False
