from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    start = 0
    balance = 0
    for i, char in enumerate(paren_string):
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        if balance == 0:
            groups.append(paren_string[start:i+1].replace(" ", ""))
            start = i+1
    return groups
