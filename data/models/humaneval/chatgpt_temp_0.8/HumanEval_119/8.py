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

    # Initialize a stack to keep track of open parentheses
    stack = []

    # Iterate over each character in the concatenated string
    for c in s:
        if c == '(':
            # Add open parentheses to the stack
            stack.append(c)
        elif c == ')':
            # If there is an open parenthesis in the stack, pop it
            # Otherwise, the string is not balanced and we return 'No'
            if stack:
                stack.pop()
            else:
                return 'No'

    # If there are no more open parentheses in the stack, the string is balanced
    # Otherwise, the string is not balanced
    if not stack:
        return 'Yes'
    else:
        return 'No'
