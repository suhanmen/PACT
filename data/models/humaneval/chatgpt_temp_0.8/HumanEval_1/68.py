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
    group_start = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                raise ValueError("Unbalanced parentheses")
            start = stack.pop()
            if not stack:
                groups.append(paren_string[group_start:i+1].replace(" ", ""))
                group_start = i+1
    if stack:
        raise ValueError("Unbalanced parentheses")
    return groups
