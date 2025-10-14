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

    # Initialize a stack to keep track of opening parentheses
    stack = []

    # Iterate over each character in the string
    for c in s:
        # If the character is an opening parenthesis, add it to the stack
        if c == '(':
            stack.append(c)
        # If the character is a closing parenthesis, check if the top of the
        # stack is a matching opening parenthesis
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                # If there is no matching opening parenthesis, return 'No'
                return 'No'
            else:
                # If there is a matching opening parenthesis, pop it from the
                # stack
                stack.pop()

    # If there are no remaining opening parentheses in the stack, return 'Yes'
    if len(stack) == 0:
        return 'Yes'
    # Otherwise, return 'No'
    else:
        return 'No'
