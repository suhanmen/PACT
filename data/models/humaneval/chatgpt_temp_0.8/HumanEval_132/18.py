def is_nested(string):
    stack = []
    for ch in string:
        if ch == '[':
            stack.append(ch)
        elif ch == ']':
            if not stack:
                continue
            if stack[-1] == '[':
                stack.pop()
                if len(stack) >= 1:
                    return True
            else:
                stack.append(ch)
    return False
