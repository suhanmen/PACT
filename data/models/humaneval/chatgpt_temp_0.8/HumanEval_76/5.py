python
def is_simple_power(x, n):
    """Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x"""
    
    if x <= 0 or n <= 0: # If either x or n is negative or zero
        return False
    
    power = 0
    while n**power <= x:
        if n**power == x:
            return True
        power += 1
        
    return False
