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

    # Using a stack to keep track of opening brackets
    stack = []

    # Loop through every character in the string
    for bracket in brackets:
        if bracket == "(":
            # If we encounter an opening bracket, add it to the stack
            stack.append(bracket)
        elif bracket == ")":
            # If we encounter a closing bracket, check if the stack is empty
            # If the stack is empty, then there is no opening bracket to match
            if not stack:
                return False
            else:
                # If the stack is not empty, pop the last opening bracket from the stack
                stack.pop()

    # After the loop is done, if the stack is empty, then every opening bracket had a corresponding closing bracket
    return not bool(stack)
