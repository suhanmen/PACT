def is_simple_power(x, n):
    if x == 1: # if x is 1, then any value of n will return True
        return True
    i = 1 # initialize i to 1
    while n**i <= x: # while n raised to i is less than or equal to x
        if n**i == x: # if n raised to i equals x, then x is a simple power of n
            return True
        i += 1 # increment i by 1
    return False # if the loop ends, it means x is not a simple power of n
