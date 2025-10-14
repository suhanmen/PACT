def is_simple_power(x, n):
    if x < n:  # if x is less than n, it can't be a power of n
        return False
    power = 1
    while power <= x:
        if power == x:  # if the current power equals x, x is a simple power of n
            return True
        power *= n  # update power by multiplying by n
    return False  # if we reach here, x is not a simple power of n
