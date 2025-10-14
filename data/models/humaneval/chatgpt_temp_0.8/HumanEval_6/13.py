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
        max_depth = 0
        cur_depth = 0
        for paren in group:
            if paren == '(':
                cur_depth += 1
                if cur_depth > max_depth:
                    max_depth = cur_depth
            elif paren == ')':
                cur_depth -= 1
        results.append(max_depth)
    return results
