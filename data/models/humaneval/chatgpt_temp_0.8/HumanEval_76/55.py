def is_simple_power(x, n):
    """
    Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x
    """
    if x == 1:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            p = 0
            while x % i == 0:
                x //= i
                p += 1
            if x == 1 and p % n == 0:
                return True
            else:
                return False
    if x != 1 and x % n == 0:
        return True
    else:
        return False
