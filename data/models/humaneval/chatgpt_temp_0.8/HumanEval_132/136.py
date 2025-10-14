def is_nested(string):
    stack = []
    nested = False
    for bracket in string:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]" and stack:
            stack.pop()
            nested = True
        elif bracket == "]" and not stack:
            continue
    return nested and bool(stack)
