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

    # initialize a stack to store the opening parentheses
    stack = []

    # iterate through the string s
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # if stack is not empty and the top element is an opening parenthesis
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                # the closing parenthesis doesn't have a matching opening parenthesis
                return 'No'
    # if the stack is empty, all parentheses are balanced
    if not stack:
        return 'Yes'
    else:
        # there are opening parentheses without a matching closing parenthesis
        return 'No'
