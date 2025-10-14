def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    s = s1 + s2
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return 'No'
    if cnt == 0:
        return 'Yes'
    else:
        return 'No'
