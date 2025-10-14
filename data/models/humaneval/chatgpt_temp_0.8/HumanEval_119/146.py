def match_parens(lst):
    # Concatenate the two strings in the list
    string = lst[0] + lst[1]
    # Use a stack to check if parentheses are balanced
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
