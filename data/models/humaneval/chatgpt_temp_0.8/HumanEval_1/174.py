python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    curr_group = ""
    for c in paren_string:
        if c == "(":
            stack.append(c)
        elif c == ")":
            stack.pop()
        curr_group += c
        if not stack:
            groups.append(curr_group.strip())
            curr_group = ""
    return groups
