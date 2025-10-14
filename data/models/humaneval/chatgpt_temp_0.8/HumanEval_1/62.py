def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    s = paren_string.replace(' ', '')  # remove any spaces
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
            if not stack:  # the stack is empty, meaning we've found a complete group
                groups.append(s[:s.index(c)+1])
                s = s[s.index(c)+1:]  # update the string to remove the processed group
    return groups
