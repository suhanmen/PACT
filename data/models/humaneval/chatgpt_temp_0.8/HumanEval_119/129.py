def match_parens(lst):
    s1 = lst[0]
    s2 = lst[1]
    s = s1 + s2
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
