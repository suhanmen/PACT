def match_parens(lst):
    # concatenate the two strings
    s = lst[0] + lst[1]
    # initialize a stack to keep track of open parentheses
    stack = []
    # iterate over the string
    for c in s:
        # if the character is an open parenthesis, push it to the stack
        if c == '(':
            stack.append(c)
        # if the character is a close parenthesis, check if the stack is empty or if the top of the stack is not an open parenthesis
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 'No'
            # if the top of the stack is an open parenthesis, pop it from the stack
            stack.pop()
    # if the stack is empty, all parentheses are balanced
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
