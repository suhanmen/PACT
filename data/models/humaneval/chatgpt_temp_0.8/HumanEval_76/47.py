python
def is_simple_power(x, n):
    """Returns True if a number x is a simple power of n, and False otherwise."""
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    return False
