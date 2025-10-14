from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize variables
    stack = []
    result = []
    start = 0
    
    # Iterate through the string
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            # Add the index of the opening parenthesis to the stack
            stack.append(i)
        elif paren_string[i] == ")":
            # If the stack is non-empty, pop the last index and append the substring to the result
            if stack:
                stack.pop()
                if not stack:
                    result.append(paren_string[start:i+1])
                    start = i+1
    
    return result
