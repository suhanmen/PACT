from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    open_count = 0
    close_count = 0
    current_group = ""
    for char in paren_string.replace(" ", ""):
        current_group += char
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        if open_count == close_count:
            groups.append(current_group)
            current_group = ""
            open_count = 0
            close_count = 0
    return groups
