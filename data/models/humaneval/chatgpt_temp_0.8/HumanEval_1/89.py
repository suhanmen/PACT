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
    result = []
    current_string = ""

    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()

        current_string += char

        if not stack:
            result.append(current_string.replace(" ", ""))
            current_string = ""

    return result
