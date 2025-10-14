python
def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
            if not stack:
                group = ''.join(stack)
                groups.append(group)
        else:
            # Ignore any spaces in the input string.
            continue
    return groups
