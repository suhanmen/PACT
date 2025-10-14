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
    
    # Initialize some variables we'll use later
    groups = []
    current_group = ""
    depth = 0
    
    # Iterate through the characters in the input string
    for char in paren_string:
        
        # If we encounter an opening parenthesis, increase the depth counter
        if char == "(":
            depth += 1
            
        # If we encounter a closing parenthesis, decrease the depth counter
        elif char == ")":
            depth -= 1
            
        # Add the current character to the current group
        current_group += char
        
        # If the depth counter is back to zero (i.e., we've closed all of the open parentheses),
        # we've found a complete group, so add it to the list of groups and reset the current group
        if depth == 0:
            groups.append(current_group)
            current_group = ""
            
    # Return the list
