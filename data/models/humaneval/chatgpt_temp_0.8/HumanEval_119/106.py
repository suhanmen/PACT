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
    first = lst[0]
    second = lst[1]
    
    # Combine the two strings
    combined = first + second
    
    # Check if the combined string has balanced parentheses
    stack = []
    for char in combined:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return 'No'
            stack.pop()
    
    if not stack:
        return 'Yes'
    else:
        return 'No'
