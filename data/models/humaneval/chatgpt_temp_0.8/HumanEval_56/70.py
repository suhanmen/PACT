# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    open_brackets = 0
    for bracket in brackets:
        if bracket == "<":
            open_brackets += 1
        elif bracket == ">":
            open_brackets -= 1
            if open_brackets < 0:
                return False
    return open_brackets == 0
