def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # check if x is even, otherwise increment it by one
    if x % 2 != 0:
        x += 1

    # check if y is even, otherwise decrement it by one
    if y % 2 != 0:
        y -= 1

    # if x is greater than y, then there's no even number in the range
    if x > y:
        return -1

    # return the biggest even number in the range
    return y
