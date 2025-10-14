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

    # Concatenate the two strings from the list
    s = lst[0] + lst[1]

    # Keep track of the number of open parentheses
    count = 0

    # Check each character in the concatenated string
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1

        # If the number of open parentheses becomes negative, return 'No'
        if count < 0:
            return 'No'

    # If the number of open parentheses is not zero, return 'No'
    if count != 0:
        return 'No'

    # Otherwise, return 'Yes'
    return 'Yes'
