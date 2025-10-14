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
    
    # initialize a stack to keep track of parentheses
    stack = []
    
    # iterate through the string
    for c in s:
        if c == '(':
            # if we encounter an open parenthesis, add it to the stack
            stack.append(c)
        elif c == ')':
            # if we encounter a close parenthesis, check if it matches the top of the stack
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                # if there is no matching open parenthesis, return 'No'
                return 'No'
    
    # if there are no remaining parentheses in the stack, the string is balanced
    if not stack:
        return 'Yes'
    else:
        return 'No'
