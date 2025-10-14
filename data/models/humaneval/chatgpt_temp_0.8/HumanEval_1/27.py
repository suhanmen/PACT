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
    parens = ""
    count = 0
    for char in paren_string.replace(" ", ""):
        parens += char
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count == 0:
                groups.append(parens)
                parens = ""
    return groups
