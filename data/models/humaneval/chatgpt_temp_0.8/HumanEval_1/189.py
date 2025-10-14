from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    count = 0
    start = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count += 1
        elif paren_string[i] == ')':
            count -= 1
        if count == 0:
            group = paren_string[start:i+1].strip()
            if group != '':
                groups.append(group)
            start = i + 1
    return groups
