from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # create an empty list to store the deepest level of nesting for each group
    max_depths = []
    # split the input string by spaces to get each group of parentheses
    groups = paren_string.split()
    # iterate through each group
    for group in groups:
        depth = 0
        max_depth = 0
        # iterate through each character in the group
        for char in group:
            # if the character is an opening parenthesis, increase the depth
            if char == '(':
                depth += 1
                # update the maximum depth if the current depth is greater
                if depth > max_depth:
                    max_depth = depth
            # if the character is a closing parenthesis, decrease the depth
            elif char == ')':
                depth -= 1
        # append the maximum depth for the current group to the max_depths list
        max_depths.append(max_depth)
    return max_depths
