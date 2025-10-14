def correct_bracketing(brackets: str):
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        elif char == ">":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
