from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        max_depth = 0
        depth = 0
        for c in group:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif c == ')':
                if depth > 0:
                    depth -= 1
                else:
                    raise ValueError('Unbalanced parentheses')
        if depth != 0:
            raise ValueError('Unbalanced parentheses')
        result.append(max_depth)
    return result
