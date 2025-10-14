def match_parens(lst):
    # Concatenate the two strings
    s = lst[0] + lst[1]
    stack = []
    
    # Traverse through the concatenated string
    for p in s:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                # If there is no opening parentheses to balance the closing one
                return 'No'
            else:
                stack.pop()
    
    # If all parentheses are balanced
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
