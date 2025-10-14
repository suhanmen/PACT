def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise."""
    if x == 1:  # Special case: 1 is a power of any number n.
        return True
    elif x < n:  # x is less than n, so x cannot be a power of n.
        return False
    else:
        # Keep dividing x by n until it is no longer divisible by n.
        # If x becomes 1, then it was a power of n; otherwise, it was not.
        while x % n == 0:
            x /= n
        return x == 1
