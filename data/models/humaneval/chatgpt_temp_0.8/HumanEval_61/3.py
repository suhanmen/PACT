def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has
    a corresponding closing bracket.
    """

    # Use a stack to track opening brackets
    stack = []

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    # If the stack is empty, all brackets are matched
    return len(stack) == 0
