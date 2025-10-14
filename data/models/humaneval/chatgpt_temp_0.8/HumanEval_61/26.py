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
    
    count = 0  # keep track of number of opening brackets
    
    for char in brackets:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:  # too many closing brackets
                return False
    
    return count == 0  # all opening brackets have a corresponding closing bracket
