def correct_bracketing(brackets: str):
    stack = []
    for b in brackets:
        if b == "<":
            stack.append(b)
        elif b == ">":
            if len(stack) == 0 or stack.pop() != "<":
                return False
    return len(stack) == 0
