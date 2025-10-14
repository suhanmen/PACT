def match_parens(lst):
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]

    # We will use a stack to keep track of the parentheses
    stack = []

    # Iterate over the string and check for balanced parentheses
    for p in s:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()

    # If there are still items in the stack, the parentheses are not balanced
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
