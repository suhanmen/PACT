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
    # Combine the two strings into one
    combined_string = lst[0] + lst[1]

    # Initialize a stack to keep track of open parentheses
    stack = []

    # Loop through each character in the combined string
    for char in combined_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis, check if the stack is empty
        # or if the top of the stack is not an open parenthesis
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                # If either condition is true, the string is not good
                return 'No'
            # If the top of the stack is an open parenthesis, pop it off the stack
            else:
                stack.pop()

    # If the stack is empty, the string is good
    if len(stack) == 0:
        return 'Yes'
    # If the stack is not empty, the string is not good
    else:
        return 'No'
