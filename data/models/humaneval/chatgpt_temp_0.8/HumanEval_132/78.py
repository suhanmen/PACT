def is_nested(string):
    stack = []
    for char in string:
        if char == "[":
            stack.append(char)
        elif char == "]":
            if len(stack) == 0:
                continue
            elif stack[-1] == "[":
                return True
            else:
                stack.pop()
    return False
