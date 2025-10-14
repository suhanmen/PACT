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
    s = lst[0] + lst[1]
    
    # Initialize a stack to keep track of opening parentheses
    stack = []
    
    # Loop through each character in the concatenated string
    for c in s:
        # If the character is an opening parenthesis, add it to the stack
        if c == '(':
            stack.append(c)
        # If the character is a closing parenthesis and there's an opening parenthesis
        # on the stack, pop the opening parenthesis from the stack
        elif c == ')' and len(stack) > 0:
            stack.pop()
        # If the character is a closing parenthesis and there's no opening parenthesis
        # on the stack, return 'No'
        else:
            return 'No'
    
    # If the stack is not empty, there are unclosed opening parentheses, so return 'No'
    if len(stack) > 0:
        return 'No'
    # Otherwise, all parentheses are balanced, so return 'Yes'
    else:
        return 'Yes'
