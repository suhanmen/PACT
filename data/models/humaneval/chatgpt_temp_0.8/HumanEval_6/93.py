from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ 
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    result = []
    groups = paren_string.split()
    for group in groups:
        max_depth = 0
        depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        result.append(max_depth)
    return result
