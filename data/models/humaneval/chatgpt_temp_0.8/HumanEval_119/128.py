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
    # count number of opening and closing parentheses in each string
    open1 = lst[0].count('(')
    close1 = lst[0].count(')')
    open2 = lst[1].count('(')
    close2 = lst[1].count(')')
    
    # check if the total number of opening and closing parentheses is even
    if (open1 + open2) % 2 == 0 and (close1 + close2) % 2 == 0:
        return 'Yes'
    else:
        return 'No'
