def match_parens(lst):
    # Concatenate the two strings
    s = ''.join(lst)

    # Initialize a stack to keep track of open parentheses
    stack = []

    # Iterate through the string
    for c in s:
        if c == '(':
            # If we encounter an open parenthesis, push it onto the stack
            stack.append(c)
        elif c == ')':
            # If we encounter a close parenthesis, pop the top element from the stack
            # and check if it matches the current character
            if len(stack) == 0 or stack.pop() != '(':
                # If the stack is empty or the top element doesn't match, return 'No'
                return 'No'

    # If the stack is empty, all parentheses are balanced and we can return 'Yes'
    return 'Yes'
