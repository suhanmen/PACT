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
    stack = []
    
    # Iterate over each character in the concatenated string
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # If the stack is empty, this means we have a closing parenthesis without a matching opening parenthesis
            if not stack:
                return 'No'
            # If the stack is not empty, pop the top element (which should be an opening parenthesis)
            # and continue iterating over the string
            stack.pop()
    
    # If the stack is empty at the end, this means all parentheses were matched and the resulting string is good
    if not stack:
        return 'Yes'
    else:
        return 'No'
