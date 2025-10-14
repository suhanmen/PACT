def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    current_group = ''
    for c in paren_string.replace(' ', ''):
        if c == '(':
            stack.append('(')
            current_group += c
        else:
            stack.pop()
            current_group += c
            if not stack:
                result.append(current_group)
                current_group = ''
    return result
