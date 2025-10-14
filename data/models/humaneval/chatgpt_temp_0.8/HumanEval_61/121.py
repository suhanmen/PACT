def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
    """
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append("(")
        elif bracket == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False
