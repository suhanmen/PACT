def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(bracket)
        if len(stack) == 0:
            return True
    return False
