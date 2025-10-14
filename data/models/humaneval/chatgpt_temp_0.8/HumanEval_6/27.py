from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    results = []
    for group in paren_string.split():
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == "(":
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ")":
                if current_depth > 0:
                    current_depth -= 1
                else:
                    # invalid parentheses
                    max_depth = -1
                    break
        if current_depth != 0:
            # invalid parentheses
            max_depth = -1
        results.append(max_depth)
    return results
