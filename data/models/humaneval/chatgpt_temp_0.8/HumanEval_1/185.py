def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove all spaces from the input string
    no_spaces = paren_string.replace(" ", "")
    
    # Initialize variables for tracking the start and end of each group
    start = 0
    end = 0
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Loop through each character in the input string
    for i, char in enumerate(no_spaces):
        # If the character is an open parenthesis, increment the count of open parens
        if char == "(":
            end = i + 1
        # If the character is a close parenthesis, decrement the count of open parens
        elif char == ")":
            # If the count of open parens is now zero, add the current group to the list of groups
            if no_spaces[start:i+1].count("(") == no_spaces[start:i+1].count(")"):
                groups.append(no_spaces[start:i+1])
                start = i + 1
    
    # Return the list of separate groups
    return groups
