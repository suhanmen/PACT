def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack:
                continue
            if stack[-1] == '[':
                return True
            else:
                while stack:
                    if stack[-1] == '[':
                        break
                    stack.pop()
                stack.pop()
    return False
