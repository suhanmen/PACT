from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        stack = []
        count = 0
        for char in group:
            if char == '(':
                stack.append(char)
                count = max(count, len(stack))
            elif char == ')':
                stack.pop()
        levels.append(count)
    return levels
