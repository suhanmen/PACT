def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    current_group = ""
    for char in paren_string:
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            stack.pop()
            current_group += char
            if not stack:
                groups.append(current_group)
                current_group = ""
        elif char == " ":
            continue
        else:
            raise ValueError("Invalid character in input string.")
    if stack:
        raise ValueError("Unbalanced parentheses in input string.")
    return groups
