def is_simple_power(x, n):
    """Return true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=k, where k is an integer.
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x == 1:  # special case when x is 1
        return True
    elif n == 1:  # special case when n is 1
        return False
    else:
        power = 1
        while power <= x:
            if power == x:
                return True
            power *= n
        return False
