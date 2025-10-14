def match_parens(lst):
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]
    stack = []
    
    # Loop through each character in the string
    for c in s:
        # If the character is an open parenthesis, add it to the stack
        if c == '(':
            stack.append(c)
        # If the character is a close parenthesis, check if the stack is empty
        elif c == ')':
            if not stack:
                return 'No'
            # If the stack is not empty, pop the top element from the stack
            stack.pop()
    
    # If the stack is empty at the end, the parentheses are balanced
    if not stack:
        return 'Yes'
    else:
        return 'No'
