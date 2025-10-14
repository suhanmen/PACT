# CANNOT PARSE CODE SNIPPET
import math

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    largest_factor = 1
    # Check if 2 is a factor and keep dividing n by 2 until it's not
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    # Check odd numbers up to the square root of n
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
    # If n is still greater than 2, it must be a prime factor
    if n > 2:
        largest_factor = n
    return largest_factor
