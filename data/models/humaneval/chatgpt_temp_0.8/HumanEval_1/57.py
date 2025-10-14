def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize some variables
    groups = []
    current_group = ""
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        
        # Add the current character to the current group
        current_group += char
        
        # If we've reached a balanced group, add it to the list and start a new group
        if balance == 0:
            groups.append(current_group)
            current_group = ""
    
    return groups
