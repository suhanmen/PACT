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
    stack = []
    # iterate through the characters in s
    for c in s:
        # if the character is an open parenthesis, add it to the stack
        if c == '(':
            stack.append(c)
        # if the character is a close parenthesis, check if there's a matching open parenthesis on the stack
        elif c == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 'No' # if there's no matching open parenthesis, return 'No'
    # if all open parentheses have matching close parentheses on the stack, return 'Yes'
    return 'Yes' if len(stack) == 0 else 'No'
