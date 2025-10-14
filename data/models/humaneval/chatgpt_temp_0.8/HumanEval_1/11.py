from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []  # Initialize a stack
    result = []  # Initialize an empty list to store the results
    
    for char in paren_string.replace(" ", ""):  # Ignore white spaces
        if char == ")":
            temp = ""
            while stack[-1] != "(":
                temp = stack.pop() + temp
            stack.pop()  # Pop the opening brace from the stack
            stack.append(temp)  # Push the entire substring to the stack
        else:
            stack.append(char)  # Push the opening brace to the stack
    
    # At this point, the stack contains all the separate groups of parentheses as strings
    for elem in stack:
        result.append(elem)
    
    return result
