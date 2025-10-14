# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    opening_count = 0
    for bracket in brackets:
        if bracket == "<":
            opening_count += 1
        elif opening_count > 0:
            opening_count -= 1
        else:
            return False
    return opening_count == 0
