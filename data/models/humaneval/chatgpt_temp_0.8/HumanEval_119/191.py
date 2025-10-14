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
    concatenated = lst[0] + lst[1]

    # Use a stack to keep track of open parentheses
    stack = []

    # Iterate over the concatenated string
    for char in concatenated:
        if char == '(':
            # If the character is an open parenthesis, add it to the stack
            stack.append(char)
        elif char == ')':
            # If the character is a close parenthesis, check if a matching open
            # parenthesis exists in the stack
            if len(stack) == 0:
                # If there are no open parentheses on the stack, the string is
                # not balanced
                return 'No'
            else:
                # Otherwise, remove the matching open parenthesis from the stack
                stack.pop()

    # If the stack is empty, all parentheses have been matched and the string is balanced
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
