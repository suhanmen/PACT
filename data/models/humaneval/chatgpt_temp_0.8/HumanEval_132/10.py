def is_nested(string):
    stack = []
    for c in string:
        if c == "[":
            stack.append(c)
        elif c == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
                if len(stack) > 0:
                    return True
            else:
                stack.append(c)
    return False
