# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                # no opening bracket to match
                return False
            stack.pop()
    # check if there are any opening brackets left unmatched
    return not stack
