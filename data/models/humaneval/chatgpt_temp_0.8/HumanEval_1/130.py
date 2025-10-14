python
def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize the variables
    groups = []
    start = 0
    stack = []
    
    # Iterate over the characters in the string
    for i, c in enumerate(paren_string):
        if c == "(":
            stack.append(c)
        elif c == ")":
            stack.pop()
            if not stack:
                # Found a complete group
                groups.append(paren_string[start:i+1])
                start = i+1
    
    return groups
