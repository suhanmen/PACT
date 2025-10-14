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
    str1, str2 = lst[0], lst[1]
    count1, count2 = 0, 0
    for paren in str1:
        if paren == '(':
            count1 += 1
        else:
            count1 -= 1
            if count1 < 0:
                return 'No'
    for paren in str2:
        if paren == '(':
            count2 += 1
        else:
            count2 -= 1
            if count2 < 0:
                return 'No'
    if count1 + count2 == 0:
        return 'Yes'
    else:
        return 'No'
