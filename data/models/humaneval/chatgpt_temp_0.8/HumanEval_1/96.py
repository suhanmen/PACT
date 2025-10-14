from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '') # Remove spaces from the input string
    groups = paren_string.split(')(') # Split the string into separate groups
    groups[0] = groups[0].lstrip('(') # Remove the opening brace from the first group
    groups[-1] = groups[-1].rstrip(')') # Remove the closing brace from the last group
    result = [group + ')' for group in groups[:-1]] + [groups[-1]] # Re-add the closing brace to each group
    return result
