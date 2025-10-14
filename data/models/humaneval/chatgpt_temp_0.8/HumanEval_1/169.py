from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to hold the separate groups of parentheses
    paren_groups = []
    
    # Keep track of the number of open and closed parentheses in the current group
    open_parens = 0
    closed_parens = 0
    
    # Keep track of the start position of the current group
    start_pos = 0
    
    # Iterate over each character in the input string
    for i, char in enumerate(paren_string):
        if char == "(":
            open_parens += 1
        elif char == ")":
            closed_parens += 1
        
        # If the number of open and closed parentheses is equal and greater than 0, we have a complete group
        if open_parens == closed_parens and open_parens > 0:
            # Add the current group to the list and reset the counters
            paren_groups.append(paren_string[start_pos:i+1])
            open_parens = 0
            closed_parens = 0
        
