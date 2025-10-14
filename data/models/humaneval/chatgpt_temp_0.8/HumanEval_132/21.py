def is_nested(string):
    stack = []
    for c in string:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
    return len(stack) < len(string) and any(s in stack for s in ['[', ']'])
