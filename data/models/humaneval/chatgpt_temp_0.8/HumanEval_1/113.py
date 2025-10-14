from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = ""
    paren_count = 0
    for char in paren_string:
        if char == "(":
            paren_count += 1
            current_group += char
        elif char == ")":
            paren_count -= 1
            current_group += char
        if paren_count == 0 and current_group:
            groups.append(current_group)
            current_group = ""
            
    return groups
