python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    current_group = ''

    # Remove all spaces from the input string
    paren_string = paren_string.replace(' ', '')

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            stack.pop()
            current_group += char
            if not stack:
                groups.append(current_group)
                current_group = ''

    return groups
