from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    # Split the input string into groups of nested parentheses
    groups = paren_string.split(' ')

    # Initialize a list to store the maximum nesting level for each group
    max_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a counter for the current nesting level
        current_level = 0
        # Initialize a counter for the maximum nesting level
        max_level = 0
        # Iterate over each character in the group
        for char in group:
            if char == '(':
                # Increment the current nesting level
                current_level += 1
                # Update the maximum nesting level if current level is greater
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                # Decrement the current nesting level
                current_level -= 1
        # Append the maximum nesting level for this group to the list
        
