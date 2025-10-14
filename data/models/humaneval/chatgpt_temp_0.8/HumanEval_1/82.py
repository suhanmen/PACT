def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    count = 0  # counts the number of open parentheses seen so far
    start = 0  # start index of the current group
    for i, c in enumerate(paren_string):
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count == 0:  # found a complete group
            groups.append(paren_string[start:i+1].replace(' ', ''))
            start = i+1
    return groups
