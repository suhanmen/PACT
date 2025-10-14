def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x == 1 or n == 1:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            j = 0
            while x % i == 0:
                x //= i
                j += 1
            if x == 1 and j % n == 0:
                return True
            elif x != 1 and j % n != 0:
                return True
    return False
