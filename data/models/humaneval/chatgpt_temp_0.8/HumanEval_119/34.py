def match_parens(lst):
    # concatenate both strings
    s = lst[0] + lst[1]

    # initialize a stack to keep track of open parentheses
    stack = []

    # loop through each character in the string
    for c in s:
        if c == '(':
            stack.append(c)  # add to the stack
        elif c == ')':
            if stack:  # if there's an open parentheses in the stack
                stack.pop()  # remove it
            else:
                return 'No'  # if stack is empty, the parentheses are not balanced

    # check if the stack is empty (all parentheses have been matched)
    if not stack:
        return 'Yes'
    else:
        return 'No'
