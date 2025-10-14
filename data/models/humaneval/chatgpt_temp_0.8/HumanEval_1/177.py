from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')  # remove any spaces from the input string
    groups = []  # list to hold each separate group of parens
    start = 0  # starting index of the current group
    count = 0  # count of open parens in the current group
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count += 1
        elif paren_string[i] == ')':
            count -= 1
            if count == 0:  # we've found a complete group
                group = paren_string[start:i+1]
                groups.append(group)
                start = i + 1
    return groups
