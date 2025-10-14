def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Given a string containing multiple groups of nested parentheses, separate those groups into separate strings
    and return the list of those strings. Separate groups are balanced (each open brace is properly closed) and not
    nested within each other. Ignore any spaces in the input string.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    # Initialize an empty list to store the result
    result = []
    # Initialize a stack to keep track of opening parentheses
    stack = []
    # Initialize a pointer to the start of the current group
    start = 0
    # Iterate over the string
    for i in range(len(paren_string)):
        # If we encounter an opening bracket, push it onto the stack
        if paren_string[i] == "(":
            stack.append(i)
        # If we encounter a closing bracket
        elif paren_string[i] == ")":
            # Pop the index of the opening bracket from the stack
            opening_bracket
