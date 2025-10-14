def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string for easier processing
    paren_string = paren_string.replace(" ", "")
    result = []
    stack = []
    current_group = ""

    # Iterate through each character in the input string
    for char in paren_string:
        if char == "(":
            # If we encounter an open parenthesis, add it to the stack and the current group
            stack.append(char)
            current_group += char
        elif char == ")":
            # If we encounter a closing parenthesis, remove the last open parenthesis from the stack and the current group
            stack.pop()
            current_group += char
            # If the stack is now empty, we have closed a complete group of parentheses
            if not stack:
                result.append(current_group)
                current_group = ""
    return result
