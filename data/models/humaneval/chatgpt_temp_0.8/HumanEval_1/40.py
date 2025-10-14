from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    group = ""
    stack = []
    groups = []
    for char in paren_string:
        if char == " ":
            continue
        group += char
        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()
            if not stack:
                groups.append(group)
                group = ""
    return groups
