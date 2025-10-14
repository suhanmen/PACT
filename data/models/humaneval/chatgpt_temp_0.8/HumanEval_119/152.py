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
    # Concatenate the two strings in the given list
    s = lst[0] + lst[1]
    
    # Use a stack to keep track of open parentheses
    stack = []
    
    # Iterate through each character in the concatenated string
    for c in s:
        if c == '(':
            # If we encounter an open parenthesis, add it to the stack
            stack.append(c)
        elif c == ')':
            # If we encounter a close parenthesis, pop the last open parenthesis from the stack
            if len(stack) > 0:
                stack.pop()
            else:
                # If there are no open parentheses left to match with, the string is not good
                return 'No'
    
    # If there are any open parentheses left in the stack, the string is not good
    if len(stack) > 0:
        return 'No'
    
    # If we made it through the entire string without any issues, the string is good
    return 'Yes'
