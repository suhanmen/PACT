from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')  # remove any spaces
    result = []
    start = 0
    end = 0
    stack = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            stack.append(paren_string[i])
        else:
            stack.pop()
        if not stack:
            end = i
            result.append(paren_string[start:end+1])
            start = i + 1
    return result
