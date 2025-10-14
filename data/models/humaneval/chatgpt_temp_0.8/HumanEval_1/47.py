from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate groups of balanced parentheses in a string into separate strings"""
    paren_string = paren_string.replace(" ", "")  # remove any spaces in the input string
    groups = []
    start = 0  # start index of a group
    balance = 0  # count of open parentheses in a group
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            balance += 1
        elif paren_string[i] == ")":
            balance -= 1
        if balance == 0:  # found balanced group
            groups.append(paren_string[start:i+1])  # add group to the list
            start = i+1  # set start index for the next group
    return groups
