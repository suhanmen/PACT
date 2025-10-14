def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # Make sure that x is the smaller number
    if x > y:
        x, y = y, x

    # Look for the biggest even number in the range
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i

    # If we get here, there was no even number in the range
    return -1
