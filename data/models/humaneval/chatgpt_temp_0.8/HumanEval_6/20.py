from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    def count_deepest_level(s: str) -> int:
        count = max_count = 0
        for c in s:
            if c == '(':
                count += 1
                max_count = max(max_count, count)
            elif c == ')':
                count -= 1
        return max_count
    
    result = []
    for group in paren_string.split():
        result.append(count_deepest_level(group))
    
    return result
