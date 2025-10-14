# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    count = 0
    for bracket in brackets:
        if bracket == "<":
            count += 1
        elif bracket == ">" and count > 0:
            count -= 1
        else:
            return False
    return count == 0
