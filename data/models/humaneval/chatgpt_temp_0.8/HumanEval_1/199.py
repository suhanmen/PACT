def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    for c in paren_string.replace(' ', ''):
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
            if not stack:
                groups.append(paren_string[:len(paren_string) - len(''.join(groups))])
    return groups
