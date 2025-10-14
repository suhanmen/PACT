# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    stack = []
    for char in brackets:
        if char == '<':
            stack.append(char)
        elif char == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
