def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    curr_group = ""

    for char in paren_string:
        if char == "(":
            stack.append(char)
            curr_group += char
        elif char == ")":
            if stack:
                stack.pop()
                curr_group += char
                if not stack:
                    groups.append(curr_group)
                    curr_group = ""
            else:
                raise ValueError("Unbalanced parentheses")
    
    if stack:
        raise ValueError("Unbalanced parentheses")
    
    return groups
