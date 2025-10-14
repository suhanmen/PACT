python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    max_depths = []
    for group in paren_string.split():
        stack = []
        depth = 0
        for paren in group:
            if paren == '(':
                stack.append(paren)
                depth = max(depth, len(stack))
            elif paren == ')':
                stack.pop()
        max_depths.append(depth)
    return max_depths
