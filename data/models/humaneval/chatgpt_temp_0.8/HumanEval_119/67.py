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
    concatenated_string = lst[0] + lst[1]

    # Use a stack to keep track of open parentheses
    stack = []

    # Iterate through the concatenated string
    for char in concatenated_string:
        if char == '(':
            # If we encounter an open parenthesis, add it to the stack
            stack.append(char)
        elif char == ')':
            # If we encounter a close parenthesis, check if the last open parenthesis
            # in the stack matches it
            if len(stack) == 0 or stack.pop() != '(':
                # If there is no matching open parenthesis, or the last open parenthesis
                # does not match the close parenthesis, the string is not good
                return 'No'

    # If we have gone through the entire string and the stack is empty, the string is good
    if len(stack) == 0:
        return 'Yes'

    # If there are still open parentheses in the stack, the string is not good
    return 'No'
