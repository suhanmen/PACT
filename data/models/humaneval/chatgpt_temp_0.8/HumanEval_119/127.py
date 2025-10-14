def match_parens(lst):
    open_count = lst[0].count('(')
    close_count = lst[0].count(')')
    
    for paren in lst[1]:
        if paren == '(':
            open_count += 1
        else:
            close_count += 1
            if close_count > open_count:
                return 'No'
    
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'
