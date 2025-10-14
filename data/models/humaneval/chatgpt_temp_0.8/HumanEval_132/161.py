def is_nested(string):
    stack = []
    for symbol in string:
        if symbol == '[':
            stack.append('[')
        elif symbol == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
    return len(stack) > 0 and ('[' in stack or ']' in stack)
