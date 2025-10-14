python
def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    result = []
    # Start with an empty string
    current = ""
    # Use a stack to keep track of opening and closing parentheses
    stack = []
    
    # Loop through each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, add it to the stack and current string
        if char == "(":
            stack.append(char)
            current += char
        # If the character is a closing parenthesis, remove its corresponding opening parenthesis from the stack
        # and add it to the current string
        elif char == ")":
            stack.pop()
            current += char
            # If the stack is empty, it means we have found a complete group of parentheses, so add the current string
            # to the result list and reset the current string
            if len(stack) == 0:
                result.append(current)
