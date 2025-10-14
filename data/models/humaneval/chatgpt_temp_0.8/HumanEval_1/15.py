from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces in the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    groups = []

    # Initialize a counter to keep track of the number of open parentheses
    open_count = 0

    # Initialize a variable to store the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the open_count counter and add the character to the current group
        if char == "(":
            open_count += 1
            current_group += char
        # If the character is a closed parenthesis, decrement the open_count counter and add the character to the current group
        elif char == ")":
            open_count -= 1
            current_group += char
        # If the open_count counter is 0 (all open parentheses have been closed), add the current group to the list
        if open_count == 
