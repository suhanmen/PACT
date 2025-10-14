def separate_paren_groups(paren_string: str) -> List[str]:
    """Separates groups of nested parentheses into separate strings.

    Args:
        paren_string: A string containing multiple groups of nested parentheses.

    Returns:
        A list of strings, where each string corresponds to a separate group of balanced parentheses
        (i.e., each open brace is properly closed).

    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize variables
    groups = []
    stack = []
    start = 0

    # Iterate through the characters of the input string
    for i, char in enumerate(paren_string):
        if char == '(':
            # Push the current index onto the stack
            stack.append(i)
        elif char == ')':
            # Pop the top index from the stack
            j = stack.pop()
            if len(stack) == 0:
                # We've found a complete group of ba
