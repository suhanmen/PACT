def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    curr_group = ''
    for c in paren_string.replace(' ', ''):
        curr_group += c
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
            if not stack:
                result.append(curr_group)
                curr_group = ''
    return result
