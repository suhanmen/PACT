def is_simple_power(x, n):
    """
    Returns True if a number x is a simple power of n and False in other cases.
    x is a simple power of n if n raised to an integer power equals x.
    For example:
    is_simple_power(1, 4) => True
    is_simple_power(2, 2) => True
    is_simple_power(8, 2) => True
    is_simple_power(3, 2) => False
    is_simple_power(3, 1) => False
    is_simple_power(5, 3) => False
    """
    if x == 1:
        return True
    for i in range(2, int(x/2)+1):
        if n**i == x:
            return True
    return False
