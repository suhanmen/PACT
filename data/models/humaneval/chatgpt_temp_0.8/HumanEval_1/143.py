def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize the result list
    result = []

    # Keep track of the current group of parentheses
    current_group = ''

    # Keep track of the number of open parentheses in the current group
    num_open_parens = 0

    # Iterate through each character in the input string
    for char in paren_string:
        if char == '(':
            # If we encounter an open parenthesis, add it to the current group
            current_group += char
            num_open_parens += 1
        elif char == ')':
            # If we encounter a close parenthesis, add it to the current group
            current_group += char
            num_open_parens -= 1
            if num_open_parens == 0:
                # If the current group is balanced, add it to the result list
                result.append(current_group)
                current_group = ''

    return result
