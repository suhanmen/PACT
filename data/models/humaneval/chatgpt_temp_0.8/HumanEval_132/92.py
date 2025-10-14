def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                continue
            if stack[-1] == '[':
                stack.pop()
                if len(stack) >= 1:
                    return True
            else:
                return False
    return False
