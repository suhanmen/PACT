def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    open_count = 0
    close_count = 0
    start_index = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        if open_count == close_count:
            groups.append(paren_string[start_index:i+1].replace(" ", ""))
            start_index = i+1
            open_count = 0
            close_count = 0
    return groups
