def match_parens(lst):
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]
    stack = []
    
    # Check if the string is good
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return 'No'
            stack.pop()
            
    if not stack:
        return 'Yes'
    else:
        return 'No'
