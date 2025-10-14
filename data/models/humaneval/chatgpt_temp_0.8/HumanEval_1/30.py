from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize some variables
    result = []
    start = 0
    count = 0
    
    # Iterate over the string, keeping track of the count of open and closed parentheses
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            count += 1
        elif paren_string[i] == ")":
            count -= 1
            
        # If we've found a complete group of parentheses, add it to the result list
        if count == 0:
            result.append(paren_string[start:i+1])
            start = i+1
            
    return result
