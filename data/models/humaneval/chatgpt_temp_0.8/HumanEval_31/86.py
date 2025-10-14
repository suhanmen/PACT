def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    
    # A number less than 2 cannot be prime
    if n < 2:
        return False
    
    # Check if n is divisible by any number from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
