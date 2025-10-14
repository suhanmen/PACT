from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")  # remove any spaces
    groups = []
    count = 0  # keep track of open parentheses
    start_index = 0  # start index of current group
    for i, char in enumerate(paren_string):
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count == 0:  # current group is complete
            groups.append(paren_string[start_index:i+1])  # add to list
            start_index = i+1  # set new start index for next group
    return groups
