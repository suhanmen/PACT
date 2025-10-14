def choose_num(x, y):
    # if x is odd, we want to start with the next even number
    if x % 2 == 1:
        x += 1
    # iterate through the range from x to y, counting by twos
    for i in range(x, y+1, 2):
        # if we find an even number, return it
        if i % 2 == 0:
            return i
    # if we reach the end of the loop without finding an even number, return -1
    return -1
