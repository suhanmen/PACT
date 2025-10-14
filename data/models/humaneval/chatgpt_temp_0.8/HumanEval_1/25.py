from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # remove any spaces in the input string
    paren_string = paren_string.replace(" ", "")
    
    # initialize variables
    groups = []
    start_index = 0
    count = 0
    
    # loop through the string
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            count += 1
        elif paren_string[i] == ")":
            count -= 1
            
        # if we've reached the end of a group, add it to the list of groups
        if count == 0:
            groups.append(paren_string[start_index:i+1])
            start_index = i+1
    
    return groups
