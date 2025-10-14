from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    result = []

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Iterate through the input string 
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            # Push the index to the stack
            stack.append(i)
        elif paren_string[i] == ')':
            # Pop the index from the stack and append the substring to the result
            if stack:
                start = stack.pop()
                if not stack:
                    result.append(paren_string[start:i+1])

    return result
