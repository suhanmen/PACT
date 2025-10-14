from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    for char in paren_string.replace(" ", ""):
        if char == "(":
            stack.append(char)
        else:
            stack.pop()
            if not stack:
                groups.append(paren_string[paren_string.index("("):paren_string.index(char)+1])
                paren_string = paren_string[paren_string.index(char)+1:]
    return groups
