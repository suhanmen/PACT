def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for ch in paren_string:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            stack.pop()
            if not stack:
                result.append(paren_string[:paren_string.index(ch) + 1])
                paren_string = paren_string[paren_string.index(ch) + 1:]
    return result
