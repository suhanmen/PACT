def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    current = ""
    for char in paren_string:
        if char == "(":
            stack.append(char)
            current += char
        elif char == ")":
            stack.pop()
            current += char
            if not stack:
                groups.append(current)
                current = ""
        elif char == " ":  # Ignore spaces
            continue
    return groups
