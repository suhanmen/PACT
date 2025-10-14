from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = ""
    stack = []
    for char in paren_string.replace(" ", ""):
        current_group += char
        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()
            if not stack:
                groups.append(current_group)
                current_group = ""
    return groups
