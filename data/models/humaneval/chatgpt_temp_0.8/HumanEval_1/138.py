def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = [group.strip() for group in paren_string.split(')') if group]
    result = []
    for group in groups:
        open_count = group.count('(')
        close_count = group.count(')')
        if open_count == close_count:
            result.append(group.replace(' ', ''))
    return result
