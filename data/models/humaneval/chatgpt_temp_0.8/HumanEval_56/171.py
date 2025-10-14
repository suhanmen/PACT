# CANNOT PARSE CODE SNIPPET
python
def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">" and len(stack) > 0:
            stack.pop()
        else:
            return False
    return len(stack) == 0
