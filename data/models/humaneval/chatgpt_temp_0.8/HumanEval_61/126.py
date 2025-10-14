def correct_bracketing(brackets: str):
    opening_brackets = 0
    for bracket in brackets:
        if bracket == "(":
            opening_brackets += 1
        elif bracket == ")":
            if opening_brackets == 0:
                return False
            opening_brackets -= 1
    return opening_brackets == 0
