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
    count = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count += 1
        elif paren_string[i] == ')':
            count -= 1
        if count == 0:
            groups.append(paren_string[:i+1])
            paren_string = paren_string[i+1:]
            i = 0
    return groups
