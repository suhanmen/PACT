def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    paren_string = paren_string.replace(" ", "") # remove spaces from input string
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()
            if not stack: # if stack is empty after popping, we have a complete group
                result.append(paren_string[:paren_string.index(char)+1])
                paren_string = paren_string[paren_string.index(char)+1:]
    return result
