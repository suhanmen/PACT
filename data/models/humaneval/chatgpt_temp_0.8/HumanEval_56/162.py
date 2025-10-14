def correct_bracketing(brackets: str):
    opening, closing = 0, 0
    for b in brackets:
        if b == "<":
            opening += 1
        elif b == ">":
            if opening > 0:
                opening -= 1
            else:
                closing += 1
    return opening == 0 and closing == 0
