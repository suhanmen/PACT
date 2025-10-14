def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    # Initialize the list of result strings
    result = []
    # Keep track of the start and end indices of each group
    start = 0
    end = 0
    # Keep track of how many open parentheses we've seen so far
    count = 0
    # Loop through the input string
    for i in range(len(paren_string)):
        # If we see an open parenthesis, increment the count
        if paren_string[i] == "(":
            count += 1
        # If we see a close parenthesis, decrement the count
        elif paren_string[i] == ")":
            count -= 1
        # If the count is 0, we've found the end of a group
        if count == 0:
            # Append the current group to the result list
            result.append(paren_string[start:i+1])
            # Move the start index to the next character
            start = i + 1
    return result
