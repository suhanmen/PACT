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
    
    # count number of open and close parentheses
    open_paren = 0
    close_paren = 0
    for paren in s:
        if paren == '(':
            open_paren += 1
        elif paren == ')':
            close_paren += 1
    
    # check if the parentheses are balanced
    if open_paren == close_paren:
        return 'Yes'
    else:
        return 'No'
