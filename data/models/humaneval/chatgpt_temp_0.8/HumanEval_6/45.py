from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    results = []
    for group in paren_string.split():
        max_level = 0
        cur_level = 0
        for char in group:
            if char == '(':
                cur_level += 1
                max_level = max(max_level, cur_level)
            elif char == ')':
                cur_level -= 1
        results.append(max_level)
    return results
