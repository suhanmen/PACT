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

    # Use a stack to keep track of opening parentheses
    stack = []

    # Iterate through each character in the concatenated string
    for c in s:
        if c == '(':
            # Push opening parentheses onto the stack
            stack.append(c)
        elif c == ')':
            # If the stack is empty or the top element is a closing parenthesis,
            # the string is not balanced and we can return 'No'
            if len(stack) == 0 or stack[-1] == ')':
                return 'No'
            # Otherwise, pop the top element from the stack
            stack.pop()

    # If the stack is empty, the string is balanced and we can return 'Yes'
    if len(stack) == 0:
        return 'Yes'
    # Otherwise, the string is not balanced and we can return 'No'
    else:
        return 'No'
