def match_parens(lst):
    # Concatenate the two strings
    s = lst[0] + lst[1]
    # Use a stack to keep track of open parentheses
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 'No'
            stack.pop()
    # If the stack is empty, all parentheses are balanced
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
