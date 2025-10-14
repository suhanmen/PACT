def is_simple_power(x, n):
    """Returns True if a number x is a simple power of n."""
    if x == 1:
        return True
    elif n == 1:
        return False
    else:
        i = 0
        while n ** i <= x:
            if n ** i == x:
                return True
            i += 1
        return False
