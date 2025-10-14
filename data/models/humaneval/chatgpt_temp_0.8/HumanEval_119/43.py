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

    # concatenate the two input strings
    s = lst[0] + lst[1]

    # use a stack to keep track of open parentheses
    stack = []

    # iterate over the string, adding open parentheses to the stack
    # and removing them when a close parenthesis is encountered
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                # if there are no open parentheses to match this close one,
                # the string is not balanced
                return 'No'
            else:
                stack.pop()

    # if there are any open parentheses left in the stack, the string is not balanced
    if len(stack) > 0:
        return 'No'
    else:
        return 'Yes'
