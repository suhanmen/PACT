def correct_bracketing(brackets: str):
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        elif char == ">":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
