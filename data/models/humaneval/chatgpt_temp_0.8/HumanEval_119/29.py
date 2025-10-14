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
    new_str = lst[0] + lst[1]

    # Counter for open parentheses
    counter = 0

    # Loop through characters in the new string
    for char in new_str:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
        if counter < 0:
            # If there are more closing parenthesis than opening parenthesis,
            # the string is not balanced
            return 'No'

    # If the counter is zero, the string is balanced
    if counter == 0:
        return 'Yes'
    else:
        return 'No'
