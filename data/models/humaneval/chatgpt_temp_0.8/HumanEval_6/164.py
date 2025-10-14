from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        max_depth = 0
        curr_depth = 0
        for char in group:
            if char == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif char == ')':
                curr_depth -= 1
        depths.append(max_depth)
    return depths
