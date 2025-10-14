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

    # Initialize a stack to keep track of the open parentheses
    stack = []

    # Iterate through the string
    for c in s:
        if c == '(':
            # If we encounter an open parenthesis, push it onto the stack
            stack.append(c)
        elif c == ')':
            # If we encounter a close parenthesis, pop the top element from the stack
            # If the stack is empty, then this close parenthesis is not balanced
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()

    # If the stack is empty at the end, then all parentheses are balanced
    # Otherwise, there are some open parentheses that are not closed
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
