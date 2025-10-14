# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    """Return True if every opening bracket has a corresponding closing bracket."""
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            stack.pop()
    return not stack
