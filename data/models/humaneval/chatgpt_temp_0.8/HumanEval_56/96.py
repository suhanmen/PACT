def correct_bracketing(brackets: str):
    opening_brackets = 0
    for bracket in brackets:
        if bracket == "<":
            opening_brackets += 1
        elif bracket == ">":
            opening_brackets -= 1
        if opening_brackets < 0:
            return False
    return opening_brackets == 0
