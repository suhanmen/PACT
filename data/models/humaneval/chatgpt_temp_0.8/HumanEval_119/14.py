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
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]
    # Use a stack to keep track of open parentheses
    stack = []
    # Iterate through each character in the concatenated string
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # If there's an open parentheses on the stack, pop it off
            # Otherwise, the string is not balanced
            if len(stack) > 0:
                stack.pop()
            else:
                return 'No'
    # If the stack is empty, the string is balanced
    # Otherwise, there are open parentheses left on the stack
    return 'Yes' if len(stack) == 0 else 'No'
