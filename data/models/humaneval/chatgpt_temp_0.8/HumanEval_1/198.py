def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()
        if not stack:
            group = "".join(groups)
            if group:
                groups.append(group)
            groups.append("")
        else:
            groups[-1] += char
    return [group.strip() for group in groups if group]
