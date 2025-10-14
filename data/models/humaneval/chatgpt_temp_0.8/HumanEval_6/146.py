from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups of nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    :param paren_string: string of nested parentheses separated by spaces
    :return: list of integers representing the maximum levels of nesting for each group of nested parentheses
    """
    levels = []
    for group in paren_string.split():
        max_level = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        levels.append(max_level)
    return levels
