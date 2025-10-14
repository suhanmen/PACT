from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    groups = []
    open_parens = 0
    current_group = ''
    
    for char in paren_string:
        if char == '(':
            open_parens += 1
        elif char == ')':
            open_parens -= 1
        
        current_group += char
        
        if open_parens == 0 and len(current_group) > 1:
            groups.append(current_group.replace(' ', ''))
            current_group = ''
        
    return groups
