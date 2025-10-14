def is_simple_power(x, n):
    if x == 1:  # Edge case where x is equal to 1
        return True
    elif n == 1:  # Edge case where n is equal to 1
        return False
    else:
        # Keep dividing x by n until x is no longer divisible by n
        while x % n == 0:
            x //= n

        # If x is reduced to 1, then it is a simple power of n
        return x == 1
