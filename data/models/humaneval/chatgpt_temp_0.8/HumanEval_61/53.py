def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []  # create an empty stack
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)  # push the opening bracket onto the stack
        elif bracket == ")":
            if len(stack) == 0:
                return False  # there is no opening bracket to match this closing bracket
            else:
                stack.pop()  # pop the last opening bracket from the stack
    return len(stack) == 0  # return True if the stack is empty, False otherwise
