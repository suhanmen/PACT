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

    # iterate over each character in s
    for c in s:
        if c == '(':
            # push opening parentheses onto the stack
            stack.append(c)
        elif c == ')':
            # if there are no opening parentheses left in the stack, then the string is not good
            if len(stack) == 0:
                return 'No'
            # pop the most recent opening parentheses from the stack
            stack.pop()

    # if there are any remaining opening parentheses in the stack, then the string is not good
    if len(stack) > 0:
        return 'No'

    # otherwise, the string is good
    return 'Yes'
