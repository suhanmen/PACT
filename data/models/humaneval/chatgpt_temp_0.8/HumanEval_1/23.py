from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    for ch in paren_string.replace(" ", ""):
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            stack.pop()
            if not stack:
                groups.append(paren_string[:len(paren_string) - len("".join(groups))])
    return groups
