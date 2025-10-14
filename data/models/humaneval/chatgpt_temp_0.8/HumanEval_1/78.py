def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')  # Remove any spaces in the input string
    result = []  # Initialize an empty list to store the separated groups

    # While there are still open parentheses in the string
    while '(' in paren_string:
        # Find the index of the first open and close parentheses
        open_index = paren_string.index('(')
        close_index = paren_string.index(')')

        # Add the substring between those parentheses to the result list
        result.append(paren_string[open_index:close_index+1])

        # Remove the substring we just added from the original string
        paren_string = paren_string[:open_index] + paren_string[close_index+1:]

    return result
