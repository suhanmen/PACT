python
def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Checks if a number is a product of 3 prime numbers."""
    if a < 2:
        return False
    factors = []
    for i in range(2, a+1):
        if is_prime(i) and a % i == 0:
            factors.append(i)
            if len(factors) > 3:
                return False
    return len(factors) == 3
