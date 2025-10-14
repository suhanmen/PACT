from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def max_depth(paren_string):
        max_depth = 0
        current_depth = 0
        for char in paren_string:
            if char == "(":
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ")":
                current_depth -= 1
        return max_depth

    groups = paren_string.split()
    depths = []
    for group in groups:
        depths.append(max_depth(group))

    return depths
