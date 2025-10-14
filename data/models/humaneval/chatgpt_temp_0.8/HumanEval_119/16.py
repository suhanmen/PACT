def match_parens(lst):
    # Concatenate the two strings in the list
    combined_str = lst[0] + lst[1]
    # Initialize a counter for open parentheses
    open_parens_count = 0
    for char in combined_str:
        if char == '(':
            open_parens_count += 1
        elif char == ')':
            # If we encounter a close parenthesis and there are no open parentheses
            # to match it with, return 'No'
            if open_parens_count == 0:
                return 'No'
            else:
                open_parens_count -= 1
    # If we reach this point and there are no open parentheses left, return 'Yes'
    if open_parens_count == 0:
        return 'Yes'
    # Otherwise, return 'No'
    else:
        return 'No'
