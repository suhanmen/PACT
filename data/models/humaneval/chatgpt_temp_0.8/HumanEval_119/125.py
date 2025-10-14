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
    concatenated_str = lst[0] + lst[1]
    
    # Initialize a stack to keep track of open parentheses
    stack = []
    
    # Iterate through the string
    for char in concatenated_str:
        if char == '(':
            # If we encounter an open parenthesis, push it onto the stack
            stack.append(char)
        elif char == ')':
            # If we encounter a close parenthesis, pop an open parenthesis off the stack
            # If the stack is empty, return 'No'
            if not stack:
                return 'No'
            stack.pop()
    
    # If the stack is empty, all parentheses were balanced
    # Otherwise, there were leftover open parentheses and the string is not good
    return 'Yes' if not stack else 'No'
