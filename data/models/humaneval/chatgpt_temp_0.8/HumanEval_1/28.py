def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    current = ""
    for char in paren_string.replace(" ", ""):
        if char == "(":
            stack.append(char)
            current += char
        elif char == ")":
            stack.pop()
            current += char
            if not stack:
                result.append(current)
                current = ""
        else:
            raise ValueError("Invalid character: {}".format(char))
    if stack:
        raise ValueError("Unbalanced parentheses")
    return result
