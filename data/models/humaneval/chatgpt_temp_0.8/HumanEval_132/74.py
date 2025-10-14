def is_nested(string):
    stack = []
    for bracket in string:
        if bracket in ['[', ']']:
            if bracket == '[':
                stack.append(bracket)
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    continue
    return not not stack
