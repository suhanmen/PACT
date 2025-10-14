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
    
    # Initialize a stack to keep track of open parentheses
    stack = []
    
    # Initialize variables to keep track of start and end indices of each group
    start = 0
    end = 0
    
    # Initialize the list of separate parentheses groups
    groups = []
    
    # Loop through each character in the input string
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            # Push the index of the open parenthesis onto the stack
            st
