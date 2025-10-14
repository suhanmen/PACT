python
def correct_bracketing(brackets: str):
    opening_brackets = 0
    for b in brackets:
        if b == "<":
            opening_brackets += 1
        elif b == ">" and opening_brackets > 0:
            opening_brackets -= 1
        else:
            return False
    return opening_brackets == 0
