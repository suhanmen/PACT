def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    s = paren_string.replace(' ', '')  # remove any spaces in the input string
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
            if not stack:
                groups.append(s[:s.index(c)+1])
                s = s[s.index(c)+1:]
    return groups
