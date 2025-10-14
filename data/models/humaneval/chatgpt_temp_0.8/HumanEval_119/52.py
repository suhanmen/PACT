def match_parens(lst):
    # Concatenate the two strings
    s = lst[0] + lst[1]
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 'No'
            stack.pop()
    if not stack:
        return 'Yes'
    else:
        return 'No'
