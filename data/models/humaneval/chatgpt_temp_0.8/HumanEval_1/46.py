from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    current = ''
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        current += char
        if len(stack) == 0:
            result.append(current.replace(' ', ''))
            current = ''
    return result
