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
    concat_str = lst[0] + lst[1]

    # Initialize a stack to keep track of opening parentheses
    stack = []

    # Iterate through the concatenated string
    for ch in concat_str:
        # If it's an opening parenthesis, push it to the stack
        if ch == '(':
            stack.append(ch)
        # If it's a closing parenthesis, check if the stack is empty or if the top element is a matching opening parenthesis
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return 'No'
            # If it's a matching opening parenthesis, pop it from the stack
            stack.pop()

    # If the stack is empty, that means all parentheses are balanced, so return 'Yes'
    if not stack:
        return 'Yes'
    else:
        return 'No'
