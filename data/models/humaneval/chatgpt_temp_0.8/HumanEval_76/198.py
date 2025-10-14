def is_simple_power(x, n):
    if x == 1:
        return True
    # Check if x is divisible by n
    while x % n == 0:
        x /= n
        # If x becomes 1, then it is a simple power of n
        if x == 1:
            return True
    # x is not a simple power of n
    return False
