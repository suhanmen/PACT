python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        max_level = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                current_level -= 1
        levels.append(max_level)
    return levels
