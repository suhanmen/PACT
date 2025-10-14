def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if n == 0:
        return 1
    else:
        result = 1
        while n > 0:
            if n % 2 == 1:
                result = (result * 2) % p
            n = n // 2
            power_of_2 = 2
            while n > 0:
                temp = (power_of_2 * power_of_2) % p
                if n % 2 == 1:
                    result = (result * power_of_2) % p
                power_of_2 = temp
                n = n // 2
    return result
