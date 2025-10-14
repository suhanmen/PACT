from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        stack = []
        max_depth = 0
        for c in group:
            if c == '(':
                stack.append(c)
                max_depth = max(max_depth, len(stack))
            elif c == ')':
                stack.pop()
        depths.append(max_depth)
    return depths
