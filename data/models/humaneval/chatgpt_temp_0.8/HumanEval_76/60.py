def is_simple_power(x, n):
    """
    Returns True if x is a simple power of n and False otherwise.
    A number x is a simple power of n if n**int = x.
    """
    if x == 1:
        return True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            p = i
            while p <= x:
                if p == x:
                    return True
                p *= i
    return False
