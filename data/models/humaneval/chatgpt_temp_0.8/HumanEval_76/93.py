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
    if x <= 0:  # x must be a positive integer
        return False
    elif x == 1:  # any number to the power of 0 is 1
        return True
    else:
        power = n
        while power <= x:
            if power == x:
                return True
            power *= n
        return False
