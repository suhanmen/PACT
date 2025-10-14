def is_nested(string):
    if len(string) < 3:  # A valid subsequence must have at least 3 brackets
        return False
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
                if len(stack) > 0:  # We found a nested bracket
                    return True
            else:
                stack.append(bracket)
    return False
