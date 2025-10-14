def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    current_group = ""
    for char in paren_string.replace(" ", ""):
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            stack.pop()
            current_group += char
            if not stack:
                groups.append(current_group)
                current_group = ""
    return groups
