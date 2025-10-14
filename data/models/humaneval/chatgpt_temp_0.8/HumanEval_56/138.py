def correct_bracketing(brackets: str):
    stack = []
    for b in brackets:
        if b == "<":
            stack.append(b)
        elif b == ">":
            if len(stack) == 0 or stack[-1] != "<":
                return False
            else:
                stack.pop()  # remove the matching opening bracket
    return len(stack) == 0  # all opening brackets must have a matching closing bracket
