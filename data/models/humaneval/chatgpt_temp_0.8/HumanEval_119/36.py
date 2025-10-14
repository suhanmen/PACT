def match_parens(lst):
    # Concatenate the two strings
    s = lst[0] + lst[1]
    stack = []
    
    # Iterate through each character in the concatenated string
    for i in s:
        if i == '(':
            # If it is an open parenthesis, add it to the stack
            stack.append(i)
        elif i == ')':
            # If it is a close parenthesis and the stack is not empty, 
            # pop the top element from the stack
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                # If the stack is empty or the top element is not an open parenthesis,
                # the string is not balanced
                return 'No'
    
    # If the stack is empty, the string is balanced
    if not stack:
        return 'Yes'
    else:
        return 'No'
