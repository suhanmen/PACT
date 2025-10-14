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
    # Iterate through each character in s
    for c in s:
        # If c is an open parenthesis, push it onto the stack
        if c == '(':
            stack.append(c)
        # If c is a close parenthesis, check if there is a matching open parenthesis on the stack.
        # If there is, pop it off the stack. If there isn't, return 'No'.
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 'No'
    # If the stack is empty at the end, all parentheses have been matched and the string is good
    if len(stack) == 0:
        return 'Yes'
    # If the stack is not empty, there are unmatched parentheses and the string is not good
    else:
        return 'No'
