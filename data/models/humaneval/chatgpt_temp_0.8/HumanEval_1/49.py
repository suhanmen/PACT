from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')  # remove spaces
    result = []
    temp = ''
    count = 0
    for c in paren_string:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        temp += c
        if count == 0:
            result.append(temp)
            temp = ''
    return result
