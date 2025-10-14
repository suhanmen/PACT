from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        stack = []
        levels.append(0)
        for char in group:
            if char == '(':
                stack.append(char)
                levels[-1] = max(levels[-1], len(stack))
            elif char == ')':
                stack.pop()

    return levels
