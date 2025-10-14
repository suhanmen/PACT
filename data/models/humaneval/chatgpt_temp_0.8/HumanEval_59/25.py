# CANNOT PARSE CODE SNIPPET
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    factor = 2
    while factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return factor
