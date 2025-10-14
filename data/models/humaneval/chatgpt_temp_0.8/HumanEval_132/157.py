def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                continue
            elif len(stack) > 0 and stack[-1] == '[':
                stack.pop()
                if len(stack) > 0:
                    return True
            else:
                continue
    return False
