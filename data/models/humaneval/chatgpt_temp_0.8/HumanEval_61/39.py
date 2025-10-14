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
    for i in range(len(brackets)):
        if brackets[i] == '(':
            stack.append('(')
        elif brackets[i] == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
