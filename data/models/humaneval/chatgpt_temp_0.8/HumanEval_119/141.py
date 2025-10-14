def match_parens(lst):
    # Concatenate the two strings into one string
    s = lst[0] + lst[1]

    # Initialize a stack to keep track of open parentheses
    stack = []

    # Iterate through the string, pushing open parentheses onto the stack
    # and popping them off when we encounter a close parentheses
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 'No'
            else:
                stack.pop()

    # If the stack is non-empty, there are unmatched open parentheses
    if len(stack) > 0:
        return 'No'
    else:
        return 'Yes'
