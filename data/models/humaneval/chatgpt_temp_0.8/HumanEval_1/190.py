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
    
    # Initialize a couple of variables to help us parse the input string
    open_count = 0
    start_idx = 0
    groups = []
    
    # Loop through each character in the input string
    for i, c in enumerate(paren_string):
        # If we encounter an opening parenthesis, increment the open_count
        if c == "(":
            open_count += 1
        # If we encounter a closing parenthesis, decrement the open_count
        elif c == ")":
            open_count -= 1
        
        # If the open_count is zero, we've found the end of a group
        if open_count == 0:
            # Extract the substring containing the current group
            group = paren_string[start_idx:i+1]
            groups.append(group)
            
            # Set the start index for the next group
            start_idx = i+1
    
    return groups
