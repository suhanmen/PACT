from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    for ch in paren_string.replace(" ", ""):
        if ch == ")":
            group = ""
            while stack[-1] != "(":
                group = stack.pop() + group
            stack.pop()  # remove "(" from stack
            stack.append(group)
        else:
            stack.append(ch)
    for group in stack:
        result.append(group)
    return result
