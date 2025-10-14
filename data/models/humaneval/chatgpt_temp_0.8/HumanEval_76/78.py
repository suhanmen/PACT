def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, False otherwise.
    """
    if x <= 0 or n <= 0:
        # x and n must be positive integers
        return False
    elif x == 1:
        # 1 is a power of any positive integer
        return True
    else:
        # Check if x is a power of n
        power = int(round(math.log(x, n)))
        return n ** power == x
