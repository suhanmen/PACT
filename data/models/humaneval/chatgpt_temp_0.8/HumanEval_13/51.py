def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Find the minimum of a and b
    minimum = min(a, b)
    
    # Iterate through all numbers from 1 to minimum
    for i in range(1, minimum+1):
        
        # Check if i divides both a and b
        if a%i == 0 and b%i == 0:
            
            # Update the greatest common divisor
            gcd = i
            
    return gcd
