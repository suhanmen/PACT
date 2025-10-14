def match_parens(lst):
    
    # concatenate the two strings
    s = lst[0] + lst[1]
    balance = 0
    
    # iterate through the concatenated string
    for char in s:
        
        # if the current character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
        
        # if the current character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
        
        # if the balance ever becomes negative, we know the string is not balanced
        if balance < 0:
            return 'No'
    
    # if the balance is zero at the end, the string is balanced
    if balance == 0:
        return 'Yes'
    else:
        return 'No'
