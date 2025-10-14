from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "") # Remove spaces from the input string
    result = []
    stack = []
    current_group = ""
    for char in paren_string:
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            stack.pop()
            current_group += char
            if not stack:
                result.append(current_group)
                current_group = ""
    return result
