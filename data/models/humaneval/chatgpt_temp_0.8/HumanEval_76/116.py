def is_simple_power(x, n):
    if x == 1: # special case where x is 1
        return True
    if n == 1 or x % n != 0: # if n is 1 or x is not divisible by n
        return False
    while x % n == 0: # keep dividing x by n until x is no longer divisible by n
        x = x // n
    return x == 1 # if x is equal to 1, then it is a simple power of n
