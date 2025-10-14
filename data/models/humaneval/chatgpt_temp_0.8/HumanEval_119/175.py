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
    string = lst[0] + lst[1]

    # Initialize a stack to keep track of open parentheses
    stack = []

    # Iterate through each character in the string
    for char in string:
        # If the character is an open parenthesis, add it to the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis, check if there's an open parenthesis on top of the stack
        elif char == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()

    # If there are no more open parentheses on the stack, return 'Yes'
    if len(stack) == 0:
        return 'Yes'
    # Otherwise, return 'No'
    else:
        return 'No'
