def is_nested(string):
    stack = []
    nested = False
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if len(stack) > 0:
                stack.pop()
                nested = True
            else:
                stack.append(bracket)
    return nested
