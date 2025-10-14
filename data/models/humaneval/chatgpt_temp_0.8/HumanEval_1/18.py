from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    opened = 0
    start = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            opened += 1
        elif char == ')':
            opened -= 1
        if opened == 0:
            groups.append(paren_string[start:i+1])
            start = i+1
    return [group.replace(' ', '') for group in groups if group != '']

