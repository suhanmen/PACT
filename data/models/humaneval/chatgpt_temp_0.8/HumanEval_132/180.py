def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if stack and stack[-1] == "[":
                return True
            else:
                stack.append(bracket)
    return False
