def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize variables
    result = []
    current_group = ''
    count = 0
    
    # Iterate through each character in the string
    for char in paren_string:
        if char == '(':
            # If it's an open parenthesis, increment the count
            count += 1
            current_group += char
        elif char == ')':
            # If it's a closed parenthesis, decrement the count
            count -= 1
            current_group += char
            if count == 0:
