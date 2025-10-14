def match_parens(lst):
    open_parens = 0
    
    for s in lst:
        for c in s:
            if c == '(':
                open_parens += 1
            else:
                if open_parens == 0:
                    return 'No'
                open_parens -= 1
    
    if open_parens == 0:
        return 'Yes'
    else:
        return 'No'
