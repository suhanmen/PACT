# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    """
    Return True if every opening bracket has a corresponding closing bracket.
    """
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                # If there's no opening bracket to match this closing bracket
                # then the string is not correctly bracketed.
                return False
            stack.pop()
    # If there are any remaining opening brackets in the stack, then the 
    # string is not correctly bracketed.
    return len(stack) == 0
