def match_parens(lst):
    s1, s2 = lst
    count = 0
    for c in s1 + s2:
        if c == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return 'No'
    return 'Yes' if count == 0 else 'No'
