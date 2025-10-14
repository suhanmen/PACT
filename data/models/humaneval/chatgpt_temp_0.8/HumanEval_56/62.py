def correct_bracketing(brackets: str):
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

    stack = []  # create an empty stack

    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)  # add opening bracket to the stack
        elif bracket == ">":
            if len(stack) == 0:  # if there is no opening bracket to match
                return False
            else:
                stack.pop()  # remove the most recent opening bracket from the stack

    if len(stack) == 0:  # if every opening bracket has a corresponding closing bracket
        return True
    else:
        return False
