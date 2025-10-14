def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if len(stack) == 0:
                continue
            if stack[-1] == "[":
                return True
            else:
                stack.pop()
    return False
