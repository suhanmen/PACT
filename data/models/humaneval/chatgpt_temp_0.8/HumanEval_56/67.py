def correct_bracketing(brackets: str):
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        elif char == ">" and stack:
            stack.pop()
        else:
            return False
    return not stack
