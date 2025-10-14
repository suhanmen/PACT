def match_parens(lst):
    # concatenate the two strings
    s = lst[0] + lst[1]
    stack = []
    # iterate through the concatenated string
    for char in s:
        if char == '(':
            # push open parentheses onto the stack
            stack.append(char)
        elif char == ')':
            # if the stack is empty or the top of the stack is a close paren, return 'No'
            if len(stack) == 0 or stack[-1] == ')':
                return 'No'
            # otherwise, pop the top of the stack (matching open paren)
            stack.pop()
    # if the stack is empty, return 'Yes'; otherwise, return 'No'
    return 'Yes' if len(stack) == 0 else 'No'
