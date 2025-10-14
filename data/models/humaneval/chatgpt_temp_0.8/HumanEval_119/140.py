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
    s = lst[0] + lst[1]
    
    # check if the number of opening and closing parentheses are the same
    # if so, then the string is balanced and we can return 'Yes'
    if s.count('(') == s.count(')'):
        return 'Yes'
    
    # if the number of opening and closing parentheses are not the same,
    # then the string is unbalanced and we can return 'No'
    else:
        return 'No'
