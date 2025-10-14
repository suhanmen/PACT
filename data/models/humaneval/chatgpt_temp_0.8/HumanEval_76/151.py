def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if x <= 0 or n <= 0:
        return False
    # keep dividing x by n until x becomes 1 or a non-integer
    while x % n == 0:
        x //= n
    # if x is 1, then it was a power of n
    return x == 1
