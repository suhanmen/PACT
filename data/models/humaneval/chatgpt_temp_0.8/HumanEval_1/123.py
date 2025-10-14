from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = ''
    count = 0
    for char in paren_string:
        if char == '(':
            count += 1
            current_group += char
        elif char == ')':
            count -= 1
            current_group += char
            if count == 0:
                groups.append(current_group)
                current_group = ''
        else:
            continue
    return groups
