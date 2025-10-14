python
def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize variables to track the start and end of each group
    start = 0
    end = 0

    # Initialize a list to store the separate groups
    groups = []

    # Loop through the input string
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            # If we find an open parenthesis, increment the end variable
            end += 1
        elif paren_string[i] == ")":
            # If we find a close parenthesis, decrement the end variable
            end -= 1
            if end == 0:
                # If end is 0, we have found the end of a group
                groups.append(paren_string[start:i+1])
                start = i+1

    return groups
