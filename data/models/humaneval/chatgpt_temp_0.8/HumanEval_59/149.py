def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest prime factor to 1
    largest_factor = 1
    # Divide the number by 2 repeatedly while it is even
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    # Check for odd factors up to the square root of n
    i = 3
    while i <= int(n ** 0.5):
        if n % i == 0:
            largest_factor = i
            n //= i
        else:
            i += 2
    # If n is still greater than 2, it must be prime
    if n > 2:
        largest_factor = n
    return largest_factor
