from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    groups = []
    current_group = ""
    for c in paren_string.replace(" ", ""):
        if c == "(":
            stack.append(c)
        elif c == ")":
            stack.pop()
        current_group += c
        if not stack:
            groups.append(current_group)
            current_group = ""
    return groups
