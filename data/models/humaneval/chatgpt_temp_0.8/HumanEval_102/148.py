def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if x is odd, if so, add 1 to make it even
    if x % 2 != 0:
        x += 1

    # Loop through the range from y to x (in reverse order) to find the first even number
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i

    # No even number found in the range [x, y]
    return -1
