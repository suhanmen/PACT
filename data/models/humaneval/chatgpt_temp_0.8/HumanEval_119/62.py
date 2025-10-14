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
    # initialize a stack to keep track of opening parentheses
    stack = []
    # iterate over each character in the string
    for c in s:
        # if the character is an opening parenthesis, push it onto the stack
        if c == '(':
            stack.append(c)
        # if the character is a closing parenthesis and there's a matching opening parenthesis on the stack, pop it
        elif c == ')' and stack and stack[-1] == '(':
            stack.pop()
        # otherwise, return 'No' since it's not possible to make a good string
        else:
            return 'No'
    # if the stack is empty, return 'Yes' since all parentheses are balanced
    if not stack:
        return 'Yes'
    # otherwise, return 'No' since there are unmatched parentheses
    else:
        return 'No'
