def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    biggest_even = -1  # initialize the biggest even number variable to -1

    # loop through the range [x, y] inclusive
    for i in range(x, y+1):
        # check if the current number is even and bigger than the current biggest even number
        if i % 2 == 0 and i > biggest_even:
            biggest_even = i

    return biggest_even
