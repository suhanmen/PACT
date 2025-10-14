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
    stack = []
    # Iterate through each character in the string
    for c in s:
        if c == '(':
            # If the character is an opening parenthesis, add it to the stack
            stack.append(c)
        elif c == ')':
            # If the character is a closing parenthesis, check if there is a matching opening parenthesis on the stack
            if len(stack) == 0:
                # If there is no opening parenthesis on the stack, return 'No'
                return 'No'
            else:
                # If there is a matching opening parenthesis on the stack, pop it off
                stack.pop()
    # If the stack is empty, all parentheses have been matched and the string is good
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
