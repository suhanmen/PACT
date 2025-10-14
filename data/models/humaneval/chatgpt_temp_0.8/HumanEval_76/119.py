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
    if x == 1:
        # 1 can be written as any power of any base, e.g., 1 = 2^0, 3^0, etc.
        # hence return True if x is 1
        return True
    elif n == 1:
        # a non-zero number raised to the power of 1 is itself
        # hence return False if n is 1 and x is not 1
        return False
    else:
        # check if x can be written as n^k for some integer k
        # if yes, return True; otherwise, return False
        k = 0
        while n**k <= x:
            if n**k == x:
                return True
            k += 1
        return False
