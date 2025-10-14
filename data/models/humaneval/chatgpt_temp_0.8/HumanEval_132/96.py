def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)
    return any(bracket in stack for bracket in '[]')
