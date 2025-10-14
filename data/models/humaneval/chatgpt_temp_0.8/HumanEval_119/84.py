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
    for c in s:
        if c == '(':
            # if we encounter an open parenthesis, add it to the stack
            stack.append(c)
        elif c == ')':
            # if we encounter a close parenthesis, check if there's a matching
            # open parenthesis on the stack
            if len(stack) == 0:
                # if there's no matching open parenthesis, the string is not good
                return 'No'
            else:
                # if there's a matching open parenthesis, pop it off the stack
                stack.pop()

    # if there are any open parentheses left on the stack, the string is not good
    if len(stack) > 0:
        return 'No'
    else:
        return 'Yes'
