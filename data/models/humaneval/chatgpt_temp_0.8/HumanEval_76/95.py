def is_simple_power(x, n):
    """
    Returns true if x is a simple power of n and false in other cases.
    x is a simple power of n if n raised to some power equals x.

    Example:
    is_simple_power(1, 4) => True
    is_simple_power(2, 2) => True
    is_simple_power(8, 2) => True
    is_simple_power(3, 2) => False
    is_simple_power(3, 1) => False
    is_simple_power(5, 3) => False
    """
    if x == 1:
        return True
    if n == 1:
        return False
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
    return False
