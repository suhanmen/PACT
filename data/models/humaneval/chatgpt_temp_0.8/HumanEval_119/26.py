def match_parens(lst):
    left_parens = 0
    for s in lst:
        for c in s:
            if c == '(':
                left_parens += 1
            else:
                if left_parens == 0:
                    return 'No'
                left_parens -= 1
    if left_parens == 0:
        return 'Yes'
    else:
        return 'No'
