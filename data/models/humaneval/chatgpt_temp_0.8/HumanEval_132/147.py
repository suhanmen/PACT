def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) == 0 or stack[-1] != '[':
                continue
            else:
                stack.pop()
                if len(stack) > 0:
                    return True
    return False
