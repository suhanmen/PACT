def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n, False otherwise.
    """
    power = int(round(math.log(x, n)))
    return n ** power == x
