from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def find_max_depth(s):
        max_depth = 0
        curr_depth = 0
        for char in s:
            if char == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif char == ')':
                curr_depth -= 1
        return max_depth
    
    result = []
    groups = paren_string.split()
    for group in groups:
        result.append(find_max_depth(group))
    return result
