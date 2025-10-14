def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif stack and stack[-1] == '[':
            stack.pop()
        elif bracket == ']':
            stack.append(bracket)
        elif stack and stack[-1] == ']':
            stack.pop()
    return len(stack) > 0 and any(bracket in stack for bracket in ['[', ']'])
