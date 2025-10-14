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
    paren_string = paren_string.replace(' ', '')
    
    # Initialize variables to keep track of parentheses
    open_paren_count = 0
    paren_start_index = 0
    paren_groups = []
    
    # Iterate through each character in the string
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            # Increase the count of open parentheses
            open_paren_count += 1
        elif paren_string[i] == ')':
            # Decrease the count of open parentheses
            open_paren_count -= 1
            if open_paren_count == 0:
                # This is the end of a balanced group of parentheses
                paren_groups.append(paren_string[paren_start_index:i+1])
                paren_start_index = i+1
                
    # Return the list of separated balanced groups of parentheses
    return paren_groups
