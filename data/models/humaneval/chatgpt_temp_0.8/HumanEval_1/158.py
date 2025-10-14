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
    stack = []
    current_str = ''
    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_str += char
        elif char == ')':
            stack.pop()
            current_str += char
            if not stack:
                result.append(current_str)
                current_str = ''
        else:
            continue
    return result
