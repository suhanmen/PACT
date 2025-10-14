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
    
    # Initialize a stack
    stack = []
    
    # Check each character in the concatenated string
    for c in s:
        # If the character is an opening parenthesis, add it to the stack
        if c == '(':
            stack.append(c)
        # If the character is a closing parenthesis, check if the stack is non-empty
        # and the top element is an opening parenthesis, then pop the top element
        # from the stack
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            # Otherwise, return 'No' as the parentheses are not balanced
            else:
                return 'No'
    
    # If the stack is empty, all parentheses are balanced
    if len(stack) == 0:
        return 'Yes'
    # Otherwise, return 'No'
    else:
        return 'No'
