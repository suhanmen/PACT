def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parens = []
    stack = []

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Iterate over the characters in the string
    for char in paren_string:
        if char == '(':
            stack.append('')
        elif char == ')':
            if len(stack) == 1:
                parens.append(stack.pop())
            else:
                curr = stack.pop()
                stack[-1] += curr[::-1] + ')'
        else:
            # Append the character to the current group
            stack[-1] += char

    # Add any remainin
