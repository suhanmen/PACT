def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    paren_count = 0
    for char in s1 + s2:
        if char == '(':
            paren_count += 1
        else:
            paren_count -= 1
        if paren_count < 0:
            return 'No'
    if paren_count == 0:
        return 'Yes'
    else:
        return 'No'
