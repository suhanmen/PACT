def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1

    # Start with the largest even number <= y
    num = y if y % 2 == 0 else y - 1

    # Iterate backwards from there and return the first even number in [x, y]
    while num >= x:
        if num % 2 == 0:
            return num
        num -= 2

    # No even number found in [x, y]
    return -1
