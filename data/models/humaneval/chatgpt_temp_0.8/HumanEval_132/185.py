def is_nested(string):
    stack = []
    for c in string:
        if c == '[':
            stack.append('[')
        elif c == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
    return len(stack) < len(string) and len(stack) > 0
