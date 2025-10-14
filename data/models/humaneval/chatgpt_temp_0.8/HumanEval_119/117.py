def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    count = 0
    for char in s1 + s2:
        if char == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return 'No'
    return 'Yes' if count == 0 else 'No'
