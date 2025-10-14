def correct_bracketing(brackets: str):
    count = 0
    for b in brackets:
        if b == '(':
            count += 1
        elif b == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
