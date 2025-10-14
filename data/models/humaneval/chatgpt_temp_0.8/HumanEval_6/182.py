from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    max_depths = []
    for group in paren_string.split():
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        max_depths.append(max_depth)
    return max_depths
