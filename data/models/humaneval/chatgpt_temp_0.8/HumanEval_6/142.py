from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Initialize an empty list to store the maximum levels of nesting for each group
    max_levels = []

    # Split the input string into separate groups
    groups = paren_string.split()

    # Iterate over each group
    for group in groups:
        # Initialize a counter to keep track of the current nesting level
        current_level = 0
        # Initialize a variable to store the maximum nesting level for this group
        max_level = 0
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting level
            if char == '(':
                current_level += 1
                # Update the maximum nesting level if necessary
                if current_level > max_level:
                    max_level = current_level
            # If the character is a closing parenthesis, decrement the current nesting level
            elif char == ')':
                current_level -= 1
