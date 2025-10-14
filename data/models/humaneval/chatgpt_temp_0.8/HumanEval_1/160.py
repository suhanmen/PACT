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
    
    # Initialize variables
    start = 0
    end = 0
    paren_groups = []
    
    # Loop through input string and find separate paren groups
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            start = i
        elif paren_string[i] == ')':
            end = i
            paren_groups.append(paren_string[start:end+1])
    
    return paren_groups
