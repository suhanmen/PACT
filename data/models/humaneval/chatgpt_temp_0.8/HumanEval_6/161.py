from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        level = max_depth = 0
        for char in group:
            if char == '(':
                level += 1
                max_depth = max(max_depth, level)
            elif char == ')':
                level -= 1
        levels.append(max_depth)
    return levels
