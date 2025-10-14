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

    # Loop through the string, ignoring any spaces
    for c in paren_string.replace(' ', ''):
        if c == '(':
            stack.append('')
        elif c == ')':
            # Pop the top of the stack and append the result to its parent
            parent = stack.pop()
            if stack:
                stack[-1] += parent + c
            else:
                result.append(parent + c)
        else:
            # Append the character to the top of the stack
            stack[-1] += c

    return result
