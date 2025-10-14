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

    # concatenate the two strings into one
    s = lst[0] + lst[1]

    # keep track of the number of open and close parentheses
    open_count = 0
    close_count = 0

    # iterate over the string and count the parentheses
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1

        # if there are more close parentheses than open parentheses,
        # the string cannot be balanced
        if close_count > open_count:
            return 'No'

    # if the number of open and close parentheses is equal, the string
    # is balanced and can be made good
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'
