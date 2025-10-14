def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        else:
            if not stack:
                continue
            stack.pop()
            if not stack:
                return True
    return False
