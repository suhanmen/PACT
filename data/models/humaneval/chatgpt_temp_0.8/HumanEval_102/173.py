def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
    """
    biggest_even = -1
    for num in range(x, y+1):
        if num % 2 == 0 and num > biggest_even:
            biggest_even = num
    return biggest_even
