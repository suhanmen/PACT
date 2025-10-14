python
def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize variables to keep track of the current group
    group_start_idx = 0
    group_stack = []

    # Iterate over the characters in the input string
    groups = []
    for i, char in enumerate(paren_string):
        if char == "(":
            group_stack.append("(")
        elif char == ")":
            group_stack.pop()
            if not group_stack:
                # We have found the end of a group
                groups.append(paren_string[group_start_idx:i+1])
                group_start_idx = i+1
    
    return groups
