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

    # concatenate the two strings
    concatenated = lst[0] + lst[1]

    # keep track of the number of open parentheses encountered
    num_open = 0

    # iterate through the concatenated string
    for char in concatenated:
        if char == '(':
            num_open += 1
        elif char == ')':
            # if there are no open parentheses to match with, return 'No'
            if num_open == 0:
                return 'No'
            else:
                num_open -= 1

    # if all open parentheses have been matched, return 'Yes', otherwise return 'No'
    if num_open == 0:
        return 'Yes'
    else:
        return 'No'
