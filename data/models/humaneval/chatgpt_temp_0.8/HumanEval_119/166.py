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

    # count the number of open and close parentheses in the two strings
    open_1 = lst[0].count('(')
    close_1 = lst[0].count(')')
    open_2 = lst[1].count('(')
    close_2 = lst[1].count(')')

    # check if the total number of open parentheses equals the total number of close parentheses
    if open_1 + open_2 == close_1 + close_2:
        return 'Yes'
    else:
        return 'No'
