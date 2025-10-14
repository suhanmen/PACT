from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        level = 0
        max_level = 0
        for char in group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        levels.append(max_level)
    return levels
