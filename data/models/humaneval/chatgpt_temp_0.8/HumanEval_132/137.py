def is_nested(string):
    stack = []
    nested = False
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack:
                stack.pop()
                nested = True
            else:
                stack.append(char)
    return nested and len(stack) != len(string)
