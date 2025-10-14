from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    for char in paren_string.replace(" ", ""):
        if char == '(':
            stack.append('')
        elif char == ')':
            result.append(''.join(stack))
            stack.pop()
        else:
            stack[-1] += char
    return result
