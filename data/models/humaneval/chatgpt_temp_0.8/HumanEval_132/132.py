def is_nested(string):
    if '[]' not in string:
        return False
    nested = False
    for i in range(len(string)):
        if string[i] == '[':
            stack = ['[']
            for j in range(i+1, len(string)):
                if string[j] == '[':
                    stack.append('[')
                elif string[j] == ']':
                    stack.pop()
                    if not stack:
                        nested = True
                        break
        if nested:
            break
    return nested
