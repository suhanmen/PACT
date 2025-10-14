def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    open_count = 0
    start = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            open_count += 1
        elif c == ')':
            open_count -= 1
            if open_count == 0:
                groups.append(paren_string[start:i+1])
                start = i+1
    return groups
