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
    
    # If x is not divisible by n, it's not a simple power
    if x % n != 0:
        return False
    
    # Divide x by n until it equals 1 (or becomes odd)
    while x > 1:
        x /= n
    
    # If x is 1, it's a simple power
    return x == 1
