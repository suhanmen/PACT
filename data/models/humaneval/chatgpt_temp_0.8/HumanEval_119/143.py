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

    string1 = lst[0]
    string2 = lst[1]
    
    count1 = string1.count('(') - string1.count(')')
    count2 = string2.count('(') - string2.count(')')
    
    if count1 + count2 == 0:
        return 'Yes'
    else:
        return 'No'
