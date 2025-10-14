def match_parens(lst):
    # count the number of open parentheses in each string
    open_1 = lst[0].count('(')
    open_2 = lst[1].count('(')
    # count the number of close parentheses in each string
    close_1 = lst[0].count(')')
    close_2 = lst[1].count(')')
    # if the total number of open and close parentheses is odd, it's impossible to make a good string
    if (open_1 + open_2 + close_1 + close_2) % 2 == 1:
        return 'No'
    # if one string has more open parentheses than the other has close parentheses,
    # or vice versa, it's impossible to make a good string
    if abs(open_1 - close_2) > open_2 or abs(close_1 - open_2) > close_2:
        return 'No'
    # otherwise, it's possible to make a good string
    return 'Yes'
