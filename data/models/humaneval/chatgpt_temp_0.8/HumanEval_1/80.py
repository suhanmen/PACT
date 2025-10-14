python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    for c in paren_string.replace(' ', ''):
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
        if not stack:
            result.append(paren_string[:len(paren_string) - len(''.join(result))])
    return result
