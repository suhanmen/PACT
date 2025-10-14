def match_parens(lst):
    # concatenate the two strings
    s = lst[0] + lst[1]
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 'No'
            else:
                stack.pop()
    return 'Yes' if not stack else 'No'
