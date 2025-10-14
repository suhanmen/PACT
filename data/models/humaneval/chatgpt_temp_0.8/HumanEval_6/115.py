from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Initialize a variable to store the maximum nesting level of parentheses for each group
    nesting_levels = []

    # Split the input string into its individual groups, separated by spaces
    groups = paren_string.split()

    # Iterate over each group and calculate its maximum nesting level
    for group in groups:
        max_nesting_level = 0
        nesting_level = 0
        for char in group:
            if char == '(':
                nesting_level += 1
                if nesting_level > max_nesting_level:
                    max_nesting_level = nesting_level
            elif char == ')':
                nesting_level -= 1
        nesting_levels.append(max_nesting_level)

    return nesting_levels
