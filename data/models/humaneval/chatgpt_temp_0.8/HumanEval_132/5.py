def is_nested(string):
    stack = []
    nested_found = False
    for char in string:
        if char == "[":
            stack.append(char)
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
                nested_found = True
            else:
                stack.append(char)
    return nested_found and bool(stack == [])
