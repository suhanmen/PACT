# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
    """
    # Use a stack to keep track of the brackets
    stack = []
    # Loop through the string
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            # If the stack is empty, then there is no matching opening bracket
            if not stack:
                return False
            # Otherwise, pop the last opening bracket from the stack
            else:
                stack.pop()
    # If the stack is empty at the end, then every opening bracket has a corresponding closing bracket
    return not stack
