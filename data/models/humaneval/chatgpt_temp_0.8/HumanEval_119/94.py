def match_parens(lst):
    stack = []  # create an empty stack
    for s in lst:  # iterate over each string in the list
        for c in s:  # iterate over each character in the string
            if c == '(':  # if it's an open parenthesis, push it onto the stack
                stack.append(c)
            else:  # if it's a close parenthesis
                if not stack:  # if the stack is empty, we can't match this close parenthesis
                    return 'No'
                else:  # otherwise, pop the top element off the stack and check if it matches the close parenthesis
                    top = stack.pop()
                    if top != '(':
                        return 'No'
    if stack:  # if there are any remaining elements in the stack, the parentheses are unbalanced
        return 'No'
    else:
        return 'Yes'
