def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest prime factor to 2
    largest_factor = 2
    # Divide n by 2 until it is no longer divisible by 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    # Check for prime factors up to the square root of n
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
    # If n is still greater than 2, it must be a prime factor
    if n > 2:
        largest_factor = n
    return largest_factor
