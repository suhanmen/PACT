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

    # concatenate the strings
    s = lst[0] + lst[1]

    # use a stack to keep track of open parentheses
    stack = []

    # iterate over each character in the concatenated string
    for c in s:
        # if we encounter an open parenthesis, push it onto the stack
        if c == '(':
            stack.append(c)
        # if we encounter a close parenthesis and the stack is not empty,
        # pop the top element from the stack (which should be an open parenthesis)
        elif c == ')' and len(stack) > 0:
            stack.pop()
        # if we encounter a close parenthesis and the stack is empty,
        # then the string is not balanced
        else:
            return 'No'

    # if the stack is empty, then the string is balanced
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
