# CANNOT PARSE CODE SNIPPET
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    """
    # Start with the smallest prime factor (2) and work our way up
    factor = 2
    while factor <= n:
        if n % factor == 0:
            # Factor found, divide n by factor and continue looking
            n //= factor
        else:
            # Factor not found, try the next one
            factor += 1
    # When the loop ends, the current factor is the largest prime factor
    return factor
