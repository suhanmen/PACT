def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    biggest_even = -1  # initialize to -1, in case there are no even numbers in range
    for i in range(x, y+1):  # loop through numbers in range
        if i % 2 == 0 and i > biggest_even:  # if i is even and bigger than previous even number found
            biggest_even = i  # update biggest_even to i
    return biggest_even
