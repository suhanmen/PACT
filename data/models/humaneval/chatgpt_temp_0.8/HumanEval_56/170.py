# CANNOT PARSE CODE SNIPPET
python
def correct_bracketing(brackets: str) -> bool:
    """Returns True if every opening bracket has a corresponding closing bracket."""
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if len(stack) == 0 or stack.pop() != "<":
                return False
    return len(stack) == 0
