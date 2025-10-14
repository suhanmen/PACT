def choose_num(x, y):
    # Check if x is even
    if x % 2 == 0:
        # If x is even, check if it's within the range [x, y]
        if x <= y:
            return y if y % 2 == 0 else y - 1
        else:
            return -1
    # If x is odd, check if x + 1 is within the range [x, y]
    elif x + 1 <= y:
        return y if y % 2 == 0 else y - 1
    else:
        return -1
