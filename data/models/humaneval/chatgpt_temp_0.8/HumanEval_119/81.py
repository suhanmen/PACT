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
    concat_str = lst[0] + lst[1]

    # use a stack to keep track of open parentheses
    stack = []

    # iterate through the concatenated string
    for char in concat_str:
        # if the character is an open parenthesis, add it to the stack
        if char == '(':
            stack.append(char)
        # if the character is a close parenthesis, check if it matches the top of the stack
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 'No'
    
    # if the stack is empty, all parentheses are balanced
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
