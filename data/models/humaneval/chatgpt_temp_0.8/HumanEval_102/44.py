def choose_num(x, y):
    # ensure x is the smaller number
    if x > y:
        x, y = y, x
    
    # iterate through the range from y to x (inclusive) backwards
    for num in range(y, x-1, -1):
        # if the number is even, return it
        if num % 2 == 0:
            return num
    
    # if no even number was found, return -1
    return -1
