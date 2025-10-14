from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # remove all spaces from paren_string
    paren_string = paren_string.replace(" ", "")

    groups = []
    # initializing variables
    left_count = 0
    right_count = 0
    group_start_index = 0

    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            left_count += 1
        elif paren_string[i] == ')':
            right_count += 1

        # if a group is balanced, add it to the list of groups
        if left_count == right_count:
            groups.append(paren_string[group_start_index:i+1])
            group_start_index = i+1

    return groups
