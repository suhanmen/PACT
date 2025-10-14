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
    
    # Initialize an empty list to store the separate groups
    result = []
    
    # Initialize a count variable to keep track of the number of open parens 
    open_count = 0
    
    # Initialize a start variable to keep track of the start of a new group
    start = 0
    
    # Loop through each character in the string
    for i in range(len(paren_string)):
        
        # If the current character is an opening parenthesis, increment the count
        if paren_string[i] == "(":
            open_count += 1
            
        # If the current character is a closing parenthesis, decrement the count
        elif paren_string[i] == ")":
            open_count -= 1
            
        # If the count is zero, we have found a complete group
        if open_count == 0:
            result.append(paren_string[start:i+1])
            start = i+1
    
    # Return the list of separate gro
