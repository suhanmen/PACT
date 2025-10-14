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

    # If the length of either string is odd, there can be no good string
    if len(lst[0]) % 2 != 0 or len(lst[1]) % 2 != 0:
        return 'No'

    # Concatenate the two strings and check if it is a good string
    str_concat = lst[0] + lst[1]
    stack = []
    for p in str_concat:
        if p == '(':
            stack.append(')')
        elif not stack or stack.pop() != p:
            return 'No'
    return 'Yes'
