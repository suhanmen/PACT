from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    results = []
    for group in paren_string.split():
        stack = []
        depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                depth = max(depth, len(stack))
            elif char == ')':
                stack.pop()
        results.append(depth)
    return results
