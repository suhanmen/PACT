from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        max_level = 0
        level = 0
        for paren in group:
            if paren == '(':
                level += 1
                max_level = max(max_level, level)
            elif paren == ')':
                level -= 1
        levels.append(max_level)
    return levels
