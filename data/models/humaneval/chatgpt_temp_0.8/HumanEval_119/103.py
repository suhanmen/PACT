def match_parens(lst):
    # Concatenate the two strings
    s = lst[0] + lst[1]
    # Keep track of the number of open parentheses
    count = 0
    # Iterate over each character in the concatenated string
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            # If there are no open parentheses to match with, return 'No'
            if count == 0:
                return 'No'
            count -= 1
    # If there are remaining open parentheses, return 'No'
    if count > 0:
        return 'No'
    return 'Yes'
