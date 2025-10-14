def match_parens(lst):
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]
    # Initialize a stack to keep track of open parentheses
    stack = []
    # Iterate through the concatenated string
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # If the stack is empty, there is no matching open parenthesis
            if not stack:
                return 'No'
            # Pop the top open parenthesis from the stack
            stack.pop()
    # If the stack is not empty, there are unmatched open parentheses
    if stack:
        return 'No'
    # Otherwise, the parentheses are balanced
    return 'Yes'
