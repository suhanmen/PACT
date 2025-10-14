from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_nesting(group: str) -> int:
        nesting = 0
        max_nesting = 0
        for char in group:
            if char == '(':
                nesting += 1
                max_nesting = max(max_nesting, nesting)
            elif char == ')':
                nesting -= 1
        return max_nesting

    groups = paren_string.split()
    return [max_nesting(group) for group in groups]
