def is_nested(string):
    stack = []
    nested_found = False
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) > 0 and stack[-1] == '[':
                nested_found = True
                stack.pop()
            else:
                stack.append(char)
    return nested_found
