def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases."""
    # check if x is equal to n raised to an integer power
    return x == n**int(round(math.log(x, n)))
