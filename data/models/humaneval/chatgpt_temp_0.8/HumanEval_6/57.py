from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        max_depth = 0
        cur_depth = 0
        for char in group:
            if char == '(':
                cur_depth += 1
                if cur_depth > max_depth:
                    max_depth = cur_depth
            elif char == ')':
                cur_depth -= 1
        depths.append(max_depth)
    return depths
