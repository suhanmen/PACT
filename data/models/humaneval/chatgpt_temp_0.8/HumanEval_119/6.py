def match_parens(lst):
    left = lst[0]
    right = lst[1]
    combined = left + right
    stack = []
    for char in combined:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return 'No'
            stack.pop()
    if not stack:
        return 'Yes'
    else:
        return 'No'
