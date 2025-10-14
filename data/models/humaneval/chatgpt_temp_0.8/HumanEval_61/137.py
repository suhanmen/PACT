def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    """
    open_brackets = 0
    
    for bracket in brackets:
        if bracket == "(":
            open_brackets += 1
        elif bracket == ")":
            open_brackets -= 1
        
        if open_brackets < 0:
            return False
    
    return open_brackets == 0
