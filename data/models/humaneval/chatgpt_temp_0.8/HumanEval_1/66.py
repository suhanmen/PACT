def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "") # remove any spaces
    paren_groups = []
    left = right = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            left += 1
        elif c == ')':
            right += 1
        if left == right:
            paren_groups.append(paren_string[:i+1])
            paren_string = paren_string[i+1:]
            left = right = 0
    return paren_groups
