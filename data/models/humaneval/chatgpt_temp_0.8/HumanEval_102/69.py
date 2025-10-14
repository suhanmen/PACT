def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:  # If x is greater than y, return -1
        return -1
    
    # Find the biggest even integer number in the range [x, y]
    for i in range(y, x-1, -1):
        if i % 2 == 0:
            return i
    
    # If there's no such number, return -1
    return -1
