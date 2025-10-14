def match_parens(lst):
    s1, s2 = lst
    # concatenate the two strings
    s = s1 + s2
    # use a stack to keep track of open parentheses
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                # there is no matching open parenthesis
                return 'No'
            stack.pop()
    if len(stack) == 0:
        # all open parentheses have been matched
        return 'Yes'
    else:
        # there are unmatched open parentheses
        return 'No'
