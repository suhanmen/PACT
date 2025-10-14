from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    for group in paren_string.split():
        stack = []
        max_level = 0
        for ch in group:
            if ch == '(':
                stack.append(ch)
                max_level = max(max_level, len(stack))
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    raise ValueError('Unbalanced parentheses')
        if stack:
            raise ValueError('Unbalanced parentheses')
        levels.append(max_level)
    return levels
