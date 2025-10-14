def match_parens(lst):
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]
    # Initialize a stack to keep track of open parentheses
    stack = []
    # Iterate over each character in the string
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # If there are no open parentheses left, return 'No'
            if not stack:
                return 'No'
            # Otherwise, remove the last open parenthesis from the stack
            stack.pop()
    # If there are any open parentheses left, return 'No'
    if stack:
        return 'No'
    # Otherwise, the string is good, so return 'Yes'
    return 'Yes'
