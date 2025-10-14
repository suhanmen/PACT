# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">" and stack:
            stack.pop()
        else:
            return False
    return not stack
