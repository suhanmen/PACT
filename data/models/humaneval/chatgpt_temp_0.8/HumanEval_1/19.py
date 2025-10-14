from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Create an empty list to store the separate groups of parentheses
    groups = []

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize a counter to keep track of the number of open parentheses
    count = 0
    start = 0

    # Iterate through the input string and check for each open and close brackets
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count += 1
        elif paren_string[i] == ')':
            count -= 1

        # When the number of open parentheses is 0, we have found a complete group
        if count == 0:
            # Append the complete group to the list of groups
            groups.append(paren_string[start:i+1])
            # Reset the start index to the next character
            start = i+1

    return groups
