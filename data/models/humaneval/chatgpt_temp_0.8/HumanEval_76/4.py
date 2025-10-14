def is_simple_power(x, n):
    """Returns True if x is a simple power of n."""
    if x == n:
        return True
    elif n == 1:
        return False
    elif n == 0:
        return x == 1
    else:
        return is_simple_power(x/n, n)
