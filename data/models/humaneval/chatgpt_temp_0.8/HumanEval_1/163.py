from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    current = ''
    
    # remove any spaces in the input string
    paren_string = paren_string.replace(' ', '')
    
    # iterate through the characters in the string
    for c in paren_string:
        if c == '(':
            stack.append(c)
            current += c
        else:
            stack.pop()
            current += c
            if not stack:
                groups.append(current)
                current = ''
    
    return groups
