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

    # Keep track of open and close parentheses
    open_count = 0
    close_count = 0

    # Iterate through the concatenated string
    for c in s:
        if c == '(':
            open_count += 1
        elif c == ')':
            close_count += 1

        # If there are more close parentheses than open parentheses, it's not a good string
        if close_count > open_count:
            return 'No'

    # If the number of open and close parentheses is equal, it's a good string
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'
