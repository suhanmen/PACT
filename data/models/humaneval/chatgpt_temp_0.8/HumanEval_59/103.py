def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest prime factor to the smallest prime number.
    largest_prime = 2
    
    # Start with the smallest prime factor and work our way up.
    factor = 2
    while factor <= n:
        # If this factor divides evenly into n, check if it's prime.
        if n % factor == 0:
            is_prime = True
            for i in range(2, factor):
                if factor % i == 0:
                    is_prime = False
                    break
            # If this factor is prime and larger than the current largest prime,
            # update the largest prime.
            if is_prime and factor > largest_prime:
                largest_prime = factor
            # Divide n by this factor and continue with the next factor.
            n //= factor
        else:
            # If this factor doesn't divide evenly into n, try the next factor.
            factor += 1
    
    return largest_prime
