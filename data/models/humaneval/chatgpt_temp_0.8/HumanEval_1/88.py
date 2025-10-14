from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []  # to store the separate groups of parentheses
    count = 0  # to keep track of the balance of parentheses
    start = 0  # to keep track of starting index of a group
    
    # iterate over every character in the string
    for i, char in enumerate(paren_string):
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            
        # if balance is zero, we have found a complete group
        if count == 0:
            # add this group to the list
            groups.append(paren_string[start:i+1].replace(" ", ""))
            # update start index for the next group
            start = i+1
    
    return groups
