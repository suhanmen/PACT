from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    groups = []
    curr_str = ''
    
    # loop through each character in the input string
    for char in paren_string:
        # ignore any spaces
        if char == ' ':
            continue
        
        curr_str += char
        
        # add the current string to the groups list if it is balanced
        if curr_str.count('(') == curr_str.count(')'):
            groups.append(curr_str)
            curr_str = ''
    
    return groups
