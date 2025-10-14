def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize variables
    factor = 2
    largest_factor = 0
    
    # Divide out all factors of 2 and update largest_factor
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    # Check for factors up to sqrt(n) and update largest_factor
    for factor in range(3, int(n ** 0.5) + 1, 2):
        while n % factor == 0:
            largest_factor = factor
            n //= factor
    
    # If n is still greater than 2, it must be prime and the largest factor
    if n > 2:
        largest_factor = n
    
    return largest_factor
