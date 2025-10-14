from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    results = []
    for group in paren_string.split():
        max_nesting = 0
        current_nesting = 0
        for char in group:
            if char == '(':
                current_nesting += 1
                if current_nesting > max_nesting:
                    max_nesting = current_nesting
            elif char == ')':
                current_nesting -= 1
        results.append(max_nesting)
    return results
