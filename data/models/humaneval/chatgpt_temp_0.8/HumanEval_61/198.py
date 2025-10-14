# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket. """
    
    count = 0
    
    for bracket in brackets:
        if bracket == "(":
            count += 1
        elif bracket == ")":
            count -= 1
            if count < 0:
                return False
    
    return count == 0
