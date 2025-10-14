from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    parens = []
    current_paren = ''
    count = 0

    for char in paren_string.replace(' ', ''):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        current_paren += char

        if count == 0:
            parens.append(current_paren)
            current_paren = ''

    return parens
