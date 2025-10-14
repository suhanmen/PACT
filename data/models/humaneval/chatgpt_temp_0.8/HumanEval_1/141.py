from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            count = 1
            j = i + 1
            while j < len(paren_string) and count > 0:
                if paren_string[j] == "(":
                    count += 1
                elif paren_string[j] == ")":
                    count -= 1
                j += 1
            groups.append(paren_string[i:j])
            i = j
        else:
            i += 1
    return groups
