from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces present in the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups of parentheses
    groups = []
    
    # Initialize two pointers to keep track of the start and end indices of each group
    start = 0
    end = 0
    
    # Iterate over the characters in the input string
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            # If an open parenthesis is encountered, increment the end pointer
            end += 1
        elif paren_string[i] == ')':
            # If a closing parenthesis is encountered, decrement the end pointer
            end -= 1
            if end == start - 1:
                # If the end pointer has reached one less than the start pointer, then we have found
                # a complete group of balanced parentheses. Add it to the list of groups.
                groups.append(paren_string[start:end+1])
                # Reset the sta
