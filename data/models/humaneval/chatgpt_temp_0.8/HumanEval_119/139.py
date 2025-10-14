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
    # concatenate the two strings
    s = lst[0] + lst[1]
    # use a stack to keep track of open parentheses
    stack = []
    # iterate through each character in the string
    for char in s:
        # if the character is an open parenthesis, add it to the stack
        if char == '(':
            stack.append(char)
        # if the character is a close parenthesis and there is an open parenthesis on the stack, pop it off
        elif char == ')' and stack:
            stack.pop()
        # if the character is a close parenthesis and there is no open parenthesis on the stack, return 'No'
        else:
            return 'No'
    # if there are no open parentheses left on the stack, return 'Yes'
    if not stack:
        return 'Yes'
    # otherwise, return 'No'
    else:
        return 'No'
