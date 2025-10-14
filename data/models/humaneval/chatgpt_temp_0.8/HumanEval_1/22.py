from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    count = 0
    start = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count == 0:
            groups.append(paren_string[start:i+1].replace(' ', ''))
            start = i+1
    return groups
