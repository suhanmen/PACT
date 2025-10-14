from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_group = ""
    open_braces = 0
    for char in paren_string.replace(" ", ""):
        current_group += char
        if char == "(":
            open_braces += 1
        elif char == ")":
            open_braces -= 1
            if open_braces == 0:
                result.append(current_group)
                current_group = ""
    return result
