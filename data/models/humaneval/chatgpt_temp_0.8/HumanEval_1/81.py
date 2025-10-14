from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    current_group = ''
    open_count = 0
    close_count = 0
    for char in paren_string:
        if char == '(':
            open_count += 1
            current_group += char
        elif char == ')':
            close_count += 1
            current_group += char
            if open_count == close_count:
                groups.append(current_group)
                current_group = ''
                open_count = 0
                close_count = 0
        else:
            continue
    return groups
