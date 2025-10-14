from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        stack = []
        max_level = 0
        for c in group:
            if c == '(':
                stack.append(c)
                max_level = max(max_level, len(stack))
            elif c == ')':
                stack.pop()
        levels.append(max_level)
    return levels
