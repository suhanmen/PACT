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
    # Initialize a stack to keep track of opening brackets
    stack = []

    # Iterate through each bracket in the input string
    for bracket in brackets:
        if bracket == "(":
            # If it's an opening bracket, push it onto the stack
            stack.append(bracket)
        elif bracket == ")":
            # If it's a closing bracket, check if there's a corresponding opening bracket on the stack
            if len(stack) == 0 or stack[-1] != "(":
                # If not, return False
                return False
            else:
                # If there is a corresponding opening bracket, pop it off the stack
                stack.pop()

    # If there are no unmatched opening brackets left on the stack, return True
    return len(stack) == 0
