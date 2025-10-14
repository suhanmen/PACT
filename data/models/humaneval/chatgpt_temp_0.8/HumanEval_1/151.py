python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_group = ''
    balance = 0
    
    # Remove all spaces from the input
    paren_string = paren_string.replace(' ', '')
    
    # Iterate through each character in the input string
    for char in paren_string:
        current_group += char
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # If the balance is zero, we have found a complete group
        if balance == 0:
            result.append(current_group)
            current_group = ''
    
    return result
