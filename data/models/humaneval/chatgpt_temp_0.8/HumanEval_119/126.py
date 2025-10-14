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
    # keep track of the balance of parentheses
    balance = 0
    # iterate over the concatenated string
    for c in s:
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
            if balance < 0:
                # if there are more closing than opening parentheses, it's not balanced
                return 'No'
    # if there are any unpaired opening parentheses, it's not balanced
    if balance != 0:
        return 'No'
    return 'Yes'
