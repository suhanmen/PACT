from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    curr_group = ""
    
    for char in paren_string.replace(" ", ""):
        if char == "(":
            stack.append(char)
            curr_group += char
        elif char == ")":
            stack.pop()
            curr_group += char
            if not stack:
                groups.append(curr_group)
                curr_group = ""
    
    return groups
