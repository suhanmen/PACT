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
    if x == 1: # Special case: any number raised to 0 is 1
        return True
    for i in range(2, x+1): # Check if n raised to each power from 2 to x is equal to x
        if n**i == x:
            return True
        elif n**i > x: # Stop searching if n raised to a power exceeds x
            return False
    return False # x is not a power of n
