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
    
    # Check each character in the concatenated string
    for char in concatenated_str:
        # If the character is an open parenthesis, add it to the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis and the stack is not empty,
        # remove the top element from the stack (matching the open parenthesis)
        elif char == ')' and len(stack) > 0:
            stack.pop()
        # If the character is a close parenthesis and the stack is empty,
        # the string is not good, so return 'No'
        elif char == ')' and len(stack) == 0:
            return 'No'
    
    # If the stack is empty, the string is good, so return 'Yes'
    if len(stack) == 0:
        return 'Yes'
    # Otherwise, the string is not good, so return 'No'
    else:
        return 'No'
