def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif len(stack) > 0:
                stack.append(char)
            else:
                stack.append(char)
    if len(stack) > 0:
        for char in stack:
            if char == '[':
                return True
        return False
    return True
