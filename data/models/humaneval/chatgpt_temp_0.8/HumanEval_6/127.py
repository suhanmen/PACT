python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for paren_group in paren_string.split():
        stack = []
        depth = 0
        for paren in paren_group:
            if paren == '(':
                stack.append('(')
                depth = max(depth, len(stack))
            elif paren == ')':
                stack.pop()
        depths.append(depth)
    return depths
