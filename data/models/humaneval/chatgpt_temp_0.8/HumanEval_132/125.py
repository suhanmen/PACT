def is_nested(string):
    stack = []
    flag = False
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                flag = True
                stack.pop()
            else:
                stack.append(char)
    return flag
