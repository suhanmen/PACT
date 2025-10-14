from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from input string
    paren_string = paren_string.replace(' ', '')

    # Initialize variables
    curr_group = ''
    groups = []

    # Iterate through characters in string
    for char in paren_string:
        curr_group += char
        if curr_group.count('(') == curr_group.count(')'):
            # Current group is balanced, add to list of groups
            groups.append(curr_group)
            curr_group = ''

    return groups
