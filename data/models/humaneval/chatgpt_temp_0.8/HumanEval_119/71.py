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
    # Concatenate the two strings
    s = lst[0] + lst[1]

    # Keep track of the balance of parentheses
    balance = 0

    # Iterate over the concatenated string
    for char in s:
        # If the current character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
        # If the current character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
        # If the balance becomes negative, the parentheses are not balanced
        if balance < 0:
            return 'No'

    # If the balance is zero, the parentheses are balanced
    if balance == 0:
        return 'Yes'
    # Otherwise, the parentheses are not balanced
    else:
        return 'No'
