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

    # Concatenate the strings
    concat_str = lst[0] + lst[1]

    # Initialize a stack to track open parentheses
    stack = []

    # Loop through the concatenated string
    for char in concat_str:
        if char == '(':
            # If the char is an open parenthesis, add it to the stack
            stack.append(char)
        elif char == ')':
            # If the char is a close parenthesis, check if there's an open parenthesis to match it
            if stack:
                stack.pop()
            else:
                # If there's no open parenthesis to match, return 'No'
                return 'No'

    # If the loop completes and there are no open parentheses left, the string is balanced
    if not stack:
        return 'Yes'
    else:
        return 'No'
