def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    open_count = 0
    current_group = ''
    for char in paren_string:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
        if open_count == 0 and current_group:
            result.append(current_group)
            current_group = ''
        if open_count > 0:
            current_group += char
    if current_group:
        result.append(current_group)
    return result
