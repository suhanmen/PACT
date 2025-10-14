def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    """
    stack = []
    for b in brackets:
        if b == "<":
            stack.append(b)
        elif b == ">":
            if not stack:
                return False
            stack.pop()
    return not stack
