def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return False
    for bracket in stack:
        if bracket == "[" or bracket == "]":
            return True
    return False
