def is_simple_power(x, n):
    if x == 1: # Special case
        return True
    elif n == 1 or x % n != 0: # x is not divisible by n or n is not greater than 1
        return False
    else:
        while x > 1: # Keep dividing x by n until it is not divisible anymore
            if x % n != 0:
                return False
            x /= n
        return True
