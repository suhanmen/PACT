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

    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif not stack:
            return False  # there is no opening bracket to match
        else:
            stack.pop()
    return not stack  # return True if stack is empty, False otherwise
