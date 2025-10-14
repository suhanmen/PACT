from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    curr_group = ''
    for char in paren_string:
        if char == ' ':
            continue
        curr_group += char
        stack.append(char)
        if len(stack) == 0:
            result.append(curr_group)
            curr_group = ''
    return result
