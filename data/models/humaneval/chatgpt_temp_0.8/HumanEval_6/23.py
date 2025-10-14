from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for paren_group in paren_string.split():
        max_level = 0
        level = 0
        for char in paren_group:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        levels.append(max_level)
    return levels
