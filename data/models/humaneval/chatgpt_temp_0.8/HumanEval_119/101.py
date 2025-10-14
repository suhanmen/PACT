def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    # Concatenate the two strings
    combined = lst[0] + lst[1]
    
    # Use a stack to keep track of open parentheses
    stack = []
    
    # Iterate through each character in the combined string
    for char in combined:
        if char == '(':
            stack.append(char)
        else:
            # If stack is empty, there is no open parenthesis to match with the closing parenthesis
            if not stack:
                return 'No'
            stack.pop()
    
    # If the stack is empty, all open parentheses have been matched and the string is good
    if not stack:
        return 'Yes'
    else:
        return 'No'
