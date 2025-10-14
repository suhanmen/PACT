def choose_num(x, y):
    # Check if x is odd, if so increment by 1 to make it even
    if x % 2 != 0:
        x += 1
    
    # Iterate from y down to x by steps of 2 to check for even numbers
    for num in range(y, x-1, -2):
        if num % 2 == 0:
            return num
    
    # No even number was found, return -1
    return -1
