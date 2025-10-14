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

    # check if there are equal number of opening and closing parentheses in both strings
    if lst[0].count('(') != lst[0].count(')') or lst[1].count('(') != lst[1].count(')'):
        return 'No'

    # if there are no closing parentheses in the first string or no opening parentheses in the second string
    # it is possible to concatenate the strings to form a good string
    if ')' not in lst[0] or '(' not in lst[1]:
        return 'Yes'

    # if the first string ends with an opening parentheses or the second string starts with a closing parentheses
    # it is not possible to concatenate the strings to form a good string
    if lst[0][-1] == '(' or lst[1][0] == ')':
        return 'No'

    return 'Yes'
