def match_parens(lst):
    # Count the number of open and close parentheses in both strings
    open_parens_1 = lst[0].count('(')
    close_parens_1 = lst[0].count(')')
    open_parens_2 = lst[1].count('(')
    close_parens_2 = lst[1].count(')')

    # If the total number of open parentheses equals the total number of close parentheses,
    # then the strings can be concatenated in some order to form a good string
    if open_parens_1 + open_parens_2 == close_parens_1 + close_parens_2:
        return 'Yes'
    else:
        return 'No'
