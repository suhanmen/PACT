def is_prime(n):
    """Helper function that returns True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implementation of the count_up_to function."""
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes
