def match_parens(lst):
    s1, s2 = lst
    # concatenate the two strings
    s = s1 + s2
    # keep track of the number of open parentheses
    num_open = 0
    for c in s:
        if c == '(':
            num_open += 1
        elif c == ')':
            if num_open == 0:
                # there's a close parenthesis without a matching open parenthesis
                return 'No'
            num_open -= 1
    # if all parentheses are balanced, num_open should be zero
    if num_open == 0:
        return 'Yes'
    else:
        return 'No'
